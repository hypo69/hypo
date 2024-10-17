## \file ../src/utils/string/product_fields_normalizer.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Модуль нормализации строк """

from typing import Union, List, Dict

from .formatter import StringFormatter
from src.logger import logger


class ProductFieldsNormalizer:
    """Class for normalizing product fields."""

    @staticmethod
    def normalize_active(active: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'active' field."""
        if isinstance(active, bool):
            return active
        elif isinstance(active, str):
            active_lower = active.lower()
            if active_lower == 'true':
                return True
            elif active_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_additional_delivery_times(times: str) -> str:
        """Normalize 'additional_delivery_times' field."""
        return StringFormatter.remove_line_breaks(times)[:256]

    @staticmethod
    def normalize_additional_shipping_cost(cost: Union[str, int, float]) -> Union[float, None]:
        """Normalize 'additional_shipping_cost' field."""
        try:
            return float(cost)
        except ValueError:
            return None

    @staticmethod
    def normalize_advanced_stock_management(advanced: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'advanced_stock_management' field."""
        if isinstance(advanced, bool):
            return advanced
        elif isinstance(advanced, str):
            advanced_lower = advanced.lower()
            if advanced_lower == 'true':
                return True
            elif advanced_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_affiliate_short_link(link: str) -> str:
        """Normalize 'affiliate_short_link' field."""
        return StringFormatter.remove_special_characters(link)[:256]

    @staticmethod
    def normalize_affiliate_summary(summary: str) -> str:
        """Normalize 'affiliate_summary' field."""
        return StringFormatter.remove_special_characters(summary)[:256]

    @staticmethod
    def normalize_affiliate_summary_2(summary: str) -> str:
        """Normalize 'affiliate_summary_2' field."""
        return StringFormatter.remove_special_characters(summary)[:256]

    @staticmethod
    def normalize_affiliate_text(text: str) -> str:
        """Normalize 'affiliate_text' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_affiliate_image_large(image: str) -> str:
        """Normalize 'affiliate_image_large' field."""
        return StringFormatter.remove_special_characters(image)[:256]

    @staticmethod
    def normalize_affiliate_image_medium(image: str) -> str:
        """Normalize 'affiliate_image_medium' field."""
        return StringFormatter.remove_special_characters(image)[:256]

    @staticmethod
    def normalize_affiliate_image_small(image: str) -> str:
        """Normalize 'affiliate_image_small' field."""
        return StringFormatter.remove_special_characters(image)[:256]

    @staticmethod
    def normalize_associations(associations: Dict) -> Dict:
        """Normalize 'associations' field."""
        # You need to define the specific normalization logic for associations
        # based on its structure
        # Example:
        # normalized_associations = {k: v[:256] for k, v in associations.items()}
        # return normalized_associations
        return associations  # Placeholder for now

    # Add the remaining normalize_* methods for other fields...
    # ...

    @staticmethod
    def normalize_width(width: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'width' field."""
        try:
            return float(width)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_additional_delivery_times(times: str) -> str:
        """Normalize 'additional_delivery_times' field."""
        return StringFormatter.remove_line_breaks(times)[:256]

    @staticmethod
    def normalize_additional_shipping_cost(cost: Union[str, int, float]) -> Union[float, None]:
        """Normalize 'additional_shipping_cost' field."""
        try:
            return float(cost)
        except ValueError:
            return None

    @staticmethod
    def normalize_advanced_stock_management(advanced: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'advanced_stock_management' field."""
        if isinstance(advanced, bool):
            return advanced
        elif isinstance(advanced, str):
            advanced_lower = advanced.lower()
            if advanced_lower == 'true':
                return True
            elif advanced_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_affiliate_short_link(link: str) -> str:
        """Normalize 'affiliate_short_link' field."""
        return StringFormatter.remove_special_characters(link)[:256]

    @staticmethod
    def normalize_affiliate_summary(summary: str) -> str:
        """Normalize 'affiliate_summary' field."""
        return StringFormatter.remove_special_characters(summary)[:256]

    @staticmethod
    def normalize_affiliate_summary_2(summary: str) -> str:
        """Normalize 'affiliate_summary_2' field."""
        return StringFormatter.remove_special_characters(summary)[:256]

    @staticmethod
    def normalize_affiliate_text(text: str) -> str:
        """Normalize 'affiliate_text' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_affiliate_image_large(image: str) -> str:
        """Normalize 'affiliate_image_large' field."""
        return StringFormatter.remove_special_characters(image)[:256]

    @staticmethod
    def normalize_affiliate_image_medium(image: str) -> str:
        """Normalize 'affiliate_image_medium' field."""
        return StringFormatter.remove_special_characters(image)[:256]

    @staticmethod
    def normalize_affiliate_image_small(image: str) -> str:
        """Normalize 'affiliate_image_small' field."""
        return StringFormatter.remove_special_characters(image)[:256]

    @staticmethod
    def normalize_associations(associations: Dict) -> Dict:
        """Normalize 'associations' field."""
        # You need to define the specific normalization logic for associations
        # based on its structure
        # Example:
        # normalized_associations = {k: v[:256] for k, v in associations.items()}
        # return normalized_associations
        return associations  # Placeholder for now

    @staticmethod
    def normalize_available_date(date: str) -> str:
        """Normalize 'available_date' field."""
        # You need to define the specific normalization logic for dates
        # Example:
        # return normalize_date(date)
        return date  # Placeholder for now

    @staticmethod
    def normalize_available_for_order(available: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'available_for_order' field."""
        if isinstance(available, bool):
            return available
        elif isinstance(available, str):
            available_lower = available.lower()
            if available_lower == 'true':
                return True
            elif available_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_available_later(text: str) -> str:
        """Normalize 'available_later' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_available_now(text: str) -> str:
        """Normalize 'available_now' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_cache_default_attribute(cache: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'cache_default_attribute' field."""
        if isinstance(cache, bool):
            return cache
        elif isinstance(cache, str):
            cache_lower = cache.lower()
            if cache_lower == 'true':
                return True
            elif cache_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_cache_has_attachments(cache: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'cache_has_attachments' field."""
        if isinstance(cache, bool):
            return cache
        elif isinstance(cache, str):
            cache_lower = cache.lower()
            if cache_lower == 'true':
                return True
            elif cache_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_cache_is_pack(cache: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'cache_is_pack' field."""
        if isinstance(cache, bool):
            return cache
        elif isinstance(cache, str):
            cache_lower = cache.lower()
            if cache_lower == 'true':
                return True
            elif cache_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_condition(condition: str) -> str:
        """Normalize 'condition' field."""
        return StringFormatter.remove_special_characters(condition)[:256]

    @staticmethod
    def normalize_customizable(customizable: Union[bool, str]) -> Union[bool, None]:
        """Normalize 'customizable' field."""
        if isinstance(customizable, bool):
            return customizable
        elif isinstance(customizable, str):
            customizable_lower = customizable.lower()
            if customizable_lower == 'true':
                return True
            elif customizable_lower == 'false':
                return
        return None

    @staticmethod
    def normalize_date_add(date: str) -> str:
        """Normalize 'date_add' field."""
        # You need to define the specific normalization logic for dates
        # Example:
        # return normalize_date(date)
        return date  # Placeholder for now

    @staticmethod
    def normalize_date_upd(date: str) -> str:
        """Normalize 'date_upd' field."""
        # You need to define the specific normalization logic for dates
        # Example:
        # return normalize_date(date)
        return date  # Placeholder for now

    @staticmethod
    def normalize_delivery_in_stock(delivery: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'delivery_in_stock' field."""
        try:
            return float(delivery)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_delivery_out_stock(delivery: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'delivery_out_stock' field."""
        try:
            return float(delivery)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_depth(dimensions: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'depth' field."""
        try:
            return float(dimensions)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_description(text: str) -> str:
        """Normalize 'description' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_description_short(text: str) -> str:
        """Normalize 'description_short' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_ean13(ean: str) -> str:
        """Normalize 'ean13' field."""
        return StringFormatter.remove_special_characters(ean)[:256]

    @staticmethod
    def normalize_ecotax(ecotax: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'ecotax' field."""
        try:
            return float(ecotax)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_height(dimensions: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'height' field."""
        try:
            return float(dimensions)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_how_to_use(text: str) -> str:
        """Normalize 'how_to_use' field."""
        return StringFormatter.remove_special_characters(text)[:256]

    @staticmethod
    def normalize_id_category_default(category_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_category_default' field."""
        try:
            return int(category_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_default_combination(combination_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_default_combination' field."""
        try:
            return int(combination_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_default_image(image_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_default_image' field."""
        try:
            return int(image_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_lang(lang_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_lang' field."""
        try:
            return int(lang_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_manufacturer(manufacturer_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_manufacturer' field."""
        try:
            return int(manufacturer_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_product(product_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_product' field."""
        try:
            return int(product_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_shop_default(shop_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_shop_default' field."""
        try:
            return int(shop_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_shop(shop_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_shop' field."""
        try:
            return int(shop_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_supplier(supplier_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_supplier' field."""
        try:
            """! строка очищается от символов и отдает только цифры. 
            Функция пробегает по строке и выдергивает только цифры, 
            присоединяя их одну к другой
            """
            return ''.join ( [ c for c in supplier_id if c.isdigit() ] )

        except (TypeError, ValueError) as e:
            logger.debug("Ошибка ", е)
            return None
        except Exception as е:
            logger.error("Ошибка ", е)
            return

    @staticmethod
    def normalize_id_tax(tax_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_tax' field."""
        try:
            return int(tax_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_id_type_redirected(redirect_type_id: Union[int, str]) -> Union[int, None]:
        """Normalize 'id_type_redirected' field."""
        try:
            return int(redirect_type_id)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_indexed(indexed: Union[bool, str]) -> bool:
        """Normalize 'indexed' field."""
        if isinstance(indexed, bool):
            return indexed
        elif isinstance(indexed, str):
            return indexed.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_ingredients(ingredients: str) -> str:
        """Normalize 'ingredients' field."""
        return StringFormatter.remove_special_characters(ingredients)[:256]

    @staticmethod
    def normalize_is_virtual(is_virtual: Union[bool, str]) -> bool:
        """Normalize 'is_virtual' field."""
        if isinstance(is_virtual, bool):
            return is_virtual
        elif isinstance(is_virtual, str):
            return is_virtual.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_isbn(isbn: str) -> str:
        """Normalize 'isbn' field."""
        return StringFormatter.remove_special_characters(isbn)[:256]

    @staticmethod
    def normalize_link_rewrite(link_rewrite: str) -> str:
        """Normalize 'link_rewrite' field."""
        link_rewrite = StringFormatter.remove_special_characters(link_rewrite)[:256]
        return link_rewrite.replace(' ', '_')

    @staticmethod
    def normalize_location(location: str) -> str:
        """Normalize 'location' field."""
        return StringFormatter.remove_special_characters(location)[:256]

    @staticmethod
    def normalize_low_stock_alert(alert: Union[bool, str]) -> bool:
        """Normalize 'low_stock_alert' field."""
        if isinstance(alert, bool):
            return alert
        elif isinstance(alert, str):
            return alert.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_low_stock_threshold(threshold: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'low_stock_threshold' field."""
        try:
            return float(threshold)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_meta_description(description: str) -> str:
        """Normalize 'meta_description' field."""
        return StringFormatter.remove_special_characters(description)[:256]

    @staticmethod
    def normalize_meta_keywords(keywords: str) -> str:
        """Normalize 'meta_keywords' field."""
        return StringFormatter.remove_special_characters(keywords)[:256]

    @staticmethod
    def normalize_meta_title(title: str) -> str:
        """Normalize 'meta_title' field."""
        return StringFormatter.remove_special_characters(title)[:256]

    @staticmethod
    def normalize_minimal_quantity(quantity: Union[int, str]) -> Union[int, None]:
        """Normalize 'minimal_quantity' field."""
        try:
            return int(quantity)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_mpn(mpn: str) -> str:
        """Normalize 'mpn' field."""
        return StringFormatter.remove_special_characters(mpn)[:256]

    @staticmethod
    def normalize_name(name: str) -> str:
        """Normalize 'name' field."""
        return StringFormatter.remove_special_characters(name)[:256]

    @staticmethod
    def normalize_online_only(online_only: Union[bool, str]) -> bool:
        """Normalize 'online_only' field."""
        if isinstance(online_only, bool):
            return online_only
        elif isinstance(online_only, str):
            return online_only.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_on_sale(on_sale: Union[bool, str]) -> bool:
        """Normalize 'on_sale' field."""
        if isinstance(on_sale, bool):
            return on_sale
        elif isinstance(on_sale, str):
            return on_sale.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_out_of_stock(out_of_stock: Union[bool, str]) -> bool:
        """Normalize 'out_of_stock' field."""
        if isinstance(out_of_stock, bool):
            return out_of_stock
        elif isinstance(out_of_stock, str):
            return out_of_stock.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_pack_stock_type(stock_type: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'pack_stock_type' field."""
        try:
            return float(stock_type)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_position_in_category(position: Union[int, str]) -> Union[int, None]:
        """Normalize 'position_in_category' field."""
        try:
            return int(position)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_price(price: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'price' field."""
        price = StringFormatter.clear_numbers(price)
        try:
            return float(price)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_product_type(product_type: str) -> str:
        """Normalize 'product_type' field."""
        return StringFormatter.remove_special_characters(product_type)[:256]

    @staticmethod
    def normalize_quantity(quantity: Union[int, str]) -> Union[int, None]:
        """Normalize 'quantity' field."""
        try:
            return int(quantity)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_quantity_discount(quantity_discount: Union[int, str]) -> Union[int, None]:
        """Normalize 'quantity_discount' field."""
        try:
            return int(quantity_discount)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_redirect_type(redirect_type: str) -> str:
        """Normalize 'redirect_type' field."""
        return StringFormatter.remove_special_characters(redirect_type)[:256]

    @staticmethod
    def normalize_reference(reference: str) -> str:
        """Normalize 'reference' field."""
        return StringFormatter.remove_special_characters(reference)[:256]

    @staticmethod
    def normalize_show_condition(show_condition: Union[bool, str]) -> bool:
        """Normalize 'show_condition' field."""
        if isinstance(show_condition, bool):
            return show_condition
        elif isinstance(show_condition, str):
            return show_condition.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_show_price(show_price: Union[bool, str]) -> bool:
        """Normalize 'show_price' field."""
        if isinstance(show_price, bool):
            return show_price
        elif isinstance(show_price, str):
            return show_price.lower() in ['true', '1']
        else:
            return

    @staticmethod
    def normalize_state(state: str) -> str:
        """Normalize 'state' field."""
        return StringFormatter.remove_special_characters(state)[:256]

    @staticmethod
    def normalize_supplier_reference(reference: str) -> str:
        """Normalize 'supplier_reference' field."""
        #return StringFormatter.remove_special_characters(reference)[:256]
        return reference

    @staticmethod
    def normalize_text_fields(text_fields: str) -> str:
        """Normalize 'text_fields' field."""
        #return StringFormatter.remove_special_characters(text)[:256]
        return text_fields

    @staticmethod
    def normalize_unit_price_ratio(ratio: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'unit_price_ratio' field."""
        try:
            return float(ratio)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_unity(unity: str) -> str:
        """Normalize 'unity' field."""
        return StringFormatter.remove_special_characters(unity)[:256]

    @staticmethod
    def normalize_upc(upc: str) -> str:
        """Normalize 'upc' field."""
        return StringFormatter.remove_special_characters(upc)[:256]

    @staticmethod
    def normalize_uploadable_files(files: Union[str, list]) -> Union[str, list[str]]:
        """Normalize 'uploadable_files' field."""
        if isinstance(files, list):
            return [StringFormatter.remove_special_characters(file)[:256] for file in files]
        elif isinstance(files, str):
            return StringFormatter.remove_special_characters(files)[:256]
        else:
            return files

    @staticmethod
    def normalize_visibility(visibility: Union[int, str]) -> Union[int, None]:
        """Normalize 'visibility' field."""
        try:
            return int(visibility)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_volume(volume: str) -> str:
        """Normalize 'volume' field."""
        return StringFormatter.remove_special_characters(volume)[:256]

    @staticmethod
    def normalize_weight(weight: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'weight' field."""
        try:
            return float(weight)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_wholesale_price(price: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'wholesale_price' field."""
        try:
            return float(price)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def normalize_width(width: Union[int, float, str]) -> Union[float, None]:
        """Normalize 'width' field."""
        try:
            return float(width)
        except (TypeError, ValueError):
            return None
