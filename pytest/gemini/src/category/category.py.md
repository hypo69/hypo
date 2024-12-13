```python
import pytest
from unittest.mock import MagicMock, patch
import asyncio
from pathlib import Path
import os
from typing import Dict, List
from lxml import html
import requests

from src.category.category import Category, compare_and_print_missing_keys
from src.endpoints.prestashop import PrestaCategory
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger


@pytest.fixture
def mock_api_credentials():
    return {"api_key": "test_key", "shop_url": "http://test.com"}


@pytest.fixture
def mock_driver():
    driver_mock = MagicMock()
    driver_mock.execute_locator.return_value = []
    return driver_mock


@pytest.fixture
def mock_logger():
    return MagicMock()


@pytest.fixture
def mock_j_loads():
    return MagicMock(return_value={})


@pytest.fixture
def mock_j_dumps():
    return MagicMock()


@pytest.fixture
def category_instance(mock_api_credentials, mock_logger):
    with patch("src.category.category.logger", mock_logger):
        return Category(mock_api_credentials)


@patch("src.category.category.logger")
class TestCategory:
    def test_category_initialization(self, mock_logger, mock_api_credentials):
        """Test Category object initialization."""
        category = Category(mock_api_credentials)
        assert isinstance(category, Category)
        assert isinstance(category, PrestaCategory)
        assert category.credentials == mock_api_credentials

    def test_get_parents(self, mock_logger, category_instance):
        """Test get_parents method retrieves parent categories correctly."""
        category_instance.get_list_parent_categories = MagicMock(
            return_value=[{"id": 1, "name": "Root"}]
        )
        parents = category_instance.get_parents(1, 0)
        assert parents == [{"id": 1, "name": "Root"}]
        category_instance.get_list_parent_categories.assert_called_once_with(1)

    @pytest.mark.asyncio
    async def test_crawl_categories_async_depth_zero(
        self, mock_logger, category_instance, mock_driver
    ):
        """Test crawl_categories_async method returns the category if depth is 0."""
        category = {"url": "test_url", "name": "", "presta_categories": {"default_category": 1, "additional_categories": []}, "children": {}}
        result = await category_instance.crawl_categories_async(
            "test_url", 0, mock_driver, "xpath", "dump.json", 1, category
        )
        assert result == category

    @pytest.mark.asyncio
    async def test_crawl_categories_async_no_links(
        self, mock_logger, category_instance, mock_driver
    ):
        """Test crawl_categories_async handles no category links found."""
        mock_driver.execute_locator.return_value = []
        result = await category_instance.crawl_categories_async(
            "test_url", 1, mock_driver, "xpath", "dump.json", 1
        )
        assert result["url"] == "test_url"
        mock_logger.error.assert_called_with("Failed to locate category links on test_url")

    @pytest.mark.asyncio
    async def test_crawl_categories_async_with_links(
        self, mock_logger, category_instance, mock_driver
    ):
        """Test crawl_categories_async with category links."""
        mock_driver.execute_locator.return_value = [
            ("Category 1", "url1"),
            ("Category 2", "url2"),
        ]
        mock_driver.get.return_value = None
        result = await category_instance.crawl_categories_async(
            "test_url", 1, mock_driver, "xpath", "dump.json", 1
        )
        assert result["url"] == "test_url"
        assert len(result["children"]) == 0

    @pytest.mark.asyncio
    async def test_crawl_categories_async_exception(
        self, mock_logger, category_instance, mock_driver
    ):
        """Test crawl_categories_async handles exceptions."""
        mock_driver.get.side_effect = Exception("Test exception")
        result = await category_instance.crawl_categories_async(
            "test_url", 1, mock_driver, "xpath", "dump.json", 1
        )
        assert result["url"] == "test_url"
        mock_logger.error.assert_called()

    def test_crawl_categories_depth_zero(
        self, mock_logger, category_instance, mock_driver
    ):
        """Test crawl_categories returns the category if depth is 0."""
        category = {}
        result = category_instance.crawl_categories(
            "test_url", 0, mock_driver, "xpath", "dump.json", 1, category
        )
        assert result == category

    def test_crawl_categories_no_links(
        self, mock_logger, category_instance, mock_driver, mock_j_loads, mock_j_dumps
    ):
        """Test crawl_categories handles no category links found."""
        mock_driver.execute_locator.return_value = []
        with patch("src.category.category.j_loads", mock_j_loads), patch(
            "src.category.category.j_dumps", mock_j_dumps
        ):
            result = category_instance.crawl_categories(
                "test_url", 1, mock_driver, "xpath", "dump.json", 1
            )
        assert result["url"] == "test_url"
        mock_logger.error.assert_called_with("Failed to locate category links on test_url")

    def test_crawl_categories_with_links(
        self, mock_logger, category_instance, mock_driver, mock_j_loads, mock_j_dumps
    ):
        """Test crawl_categories with category links."""
        mock_driver.execute_locator.return_value = [
            ("Category 1", "url1"),
            ("Category 2", "url2"),
        ]
        mock_driver.get.return_value = None

        with patch("src.category.category.j_loads", mock_j_loads), patch(
            "src.category.category.j_dumps", mock_j_dumps
        ):
            result = category_instance.crawl_categories(
                "test_url", 1, mock_driver, "xpath", "dump.json", 1
            )
        assert "Category 1" in result
        assert result["Category 1"]["url"] == "url1"
        assert result["Category 2"]["url"] == "url2"

    def test_crawl_categories_exception(
        self, mock_logger, category_instance, mock_driver, mock_j_loads, mock_j_dumps
    ):
        """Test crawl_categories handles exceptions."""
        mock_driver.get.side_effect = Exception("Test exception")
        with patch("src.category.category.j_loads", mock_j_loads), patch(
            "src.category.category.j_dumps", mock_j_dumps
        ):
             result = category_instance.crawl_categories(
                 "test_url", 1, mock_driver, "xpath", "dump.json", 1
             )
        assert result["url"] == "test_url"
        mock_logger.error.assert_called()

    def test_is_duplicate_url(self, mock_logger, category_instance):
        """Test _is_duplicate_url method correctly identifies duplicate URLs."""
        category = {
            "cat1": {"url": "url1"},
            "cat2": {"url": "url2"},
        }
        assert category_instance._is_duplicate_url(category, "url1") is True
        assert category_instance._is_duplicate_url(category, "url3") is False


@patch("src.category.category.logger")
class TestCompareAndPrintMissingKeys:
    def test_compare_and_print_missing_keys_success(
        self, mock_logger, mock_j_loads
    ):
        """Test compare_and_print_missing_keys successfully."""
        current_dict = {"key1": "value1", "key2": "value2"}
        mock_j_loads.return_value = {"key2": "from_file", "key3": "from_file"}
        with patch("src.category.category.j_loads", mock_j_loads), patch(
            "builtins.print"
        ) as mock_print:
            compare_and_print_missing_keys(current_dict, "test_file.json")
            mock_print.assert_called_once_with("key3")

    def test_compare_and_print_missing_keys_file_error(self, mock_logger, mock_j_loads):
        """Test compare_and_print_missing_keys when file loading fails."""
        mock_j_loads.side_effect = Exception("Test exception")
        with patch("src.category.category.j_loads", mock_j_loads):
            compare_and_print_missing_keys({}, "test_file.json")
            mock_logger.error.assert_called()
```