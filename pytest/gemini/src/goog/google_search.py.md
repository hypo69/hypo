```python
import pytest
from lxml import html
from hypotez.src.goog.google_search import GoogleHtmlParser


@pytest.fixture
def mock_html_desktop():
    """Provides a mock HTML string for desktop Google search."""
    return """
    <html>
        <body>
            <div id="result-stats">About 1,234,567 results (0.35 seconds)</div>
            <div class="g">
                <a href="https://example.com/1">
                  <h3 class="LC20lb MBeuO DKV0Md">Title 1</h3>
                </a>
                <div class="IsZvec">
                   <div class="VwiC3b yXK7lf MUxGbd lyLwlc lEBKkf" data-sncfb="0">
                      <div>
                          <div>
                             <div class="BNeawe s3v9rd AP7Wnd">
                                snippet 1
                             </div>
                          </div>
                       </div>
                       <div class="BNeawe s3v9rd AP7Wnd">
                        rich snippet 1
                       </div>
                    </div>
                </div>
            </div>
             <div class="g">
                <a href="https://example.com/2">
                  <h3 class="LC20lb MBeuO DKV0Md">Title 2</h3>
                </a>
                 <div class="IsZvec">
                   <div class="VwiC3b yXK7lf MUxGbd lyLwlc lEBKkf" data-sncfb="0">
                      <div>
                         <div class="BNeawe s3v9rd AP7Wnd">
                                snippet 2
                         </div>
                      </div>
                    </div>
                </div>
            </div>
             <div class="kp-blk">
                <h3 class="hNk7z">Featured Snippet Title</h3>
                <a href="https://example.com/featured">
                   
                </a>
            </div>
            <div class="kp-wholepage">
                <h2 class="h2"><span>Knowledge Card Title</span></h2>
                <div data-attrid="subtitle">Knowledge Card Subtitle</div>
                <div class="kno-rdesc"><span>Knowledge Card Description</span></div>
                <div data-attrid=":/"><span>Key1:</span><span>Value1</span></div>
                <div data-attrid=":/"><span>Key2:</span><span>Value2</span></div>
            </div>
             <g-section-with-header>
                <h3 class="rS95Pd">Top Stories</h3>
                 <g-inner-card>
                    <div role="heading">Top Story Title 1</div>
                    <a href="https://example.com/top_story1"></a>
                 </g-inner-card>
                <g-inner-card>
                    <div role="heading">Top Story Title 2</div>
                    <a href="https://example.com/top_story2"></a>
                 </g-inner-card>
             </g-section-with-header>
        </body>
    </html>
    """

@pytest.fixture
def mock_html_mobile():
    """Provides a mock HTML string for mobile Google search."""
    return """
    <html>
        <body>
        </body>
    </html>
    """


def test_googlehtmlparser_init_desktop(mock_html_desktop):
    """Checks if the parser initializes correctly with desktop user agent."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    assert parser.user_agent == 'desktop'
    assert isinstance(parser.tree, html.HtmlElement)


def test_googlehtmlparser_init_mobile(mock_html_mobile):
    """Checks if the parser initializes correctly with mobile user agent."""
    parser = GoogleHtmlParser(mock_html_mobile, user_agent='mobile')
    assert parser.user_agent == 'mobile'
    assert isinstance(parser.tree, html.HtmlElement)


def test_googlehtmlparser_init_default_user_agent(mock_html_desktop):
    """Checks if the parser initializes correctly with the default user agent."""
    parser = GoogleHtmlParser(mock_html_desktop)
    assert parser.user_agent == 'desktop'


def test_googlehtmlparser_init_invalid_user_agent(mock_html_desktop):
    """Checks if the parser defaults to 'desktop' for an invalid user agent."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='invalid')
    assert parser.user_agent == 'desktop'

def test_clean_with_valid_content():
    """Checks that _clean method correctly cleans a string."""
    parser = GoogleHtmlParser("<html></html>")
    content = "  test   string  "
    cleaned_content = parser._clean(content)
    assert cleaned_content == "test string"

def test_clean_with_empty_content():
    """Checks that _clean method returns an empty string when content is empty."""
    parser = GoogleHtmlParser("<html></html>")
    content = ""
    cleaned_content = parser._clean(content)
    assert cleaned_content == ""

def test_clean_with_none_content():
    """Checks that _clean method returns an empty string when content is None."""
    parser = GoogleHtmlParser("<html></html>")
    content = None
    cleaned_content = parser._clean(content)
    assert cleaned_content == ""


def test_normalize_dict_key():
    """Checks that _normalize_dict_key method correctly formats the string."""
    parser = GoogleHtmlParser("<html></html>")
    content = "Test String: with colon "
    normalized_key = parser._normalize_dict_key(content)
    assert normalized_key == "test_string_with_colon"


def test_get_estimated_results(mock_html_desktop):
    """Checks that _get_estimated_results correctly extracts the number of results."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    estimated_results = parser._get_estimated_results()
    assert estimated_results == 1234567


def test_get_estimated_results_no_element():
    """Checks that _get_estimated_results returns 0 when the element is not found."""
    parser = GoogleHtmlParser("<html><body></body></html>", user_agent='desktop')
    estimated_results = parser._get_estimated_results()
    assert estimated_results == 0


def test_get_organic(mock_html_desktop):
    """Checks that _get_organic returns the organic search results correctly."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    organic_results = parser._get_organic()
    assert len(organic_results) == 2
    assert organic_results[0]['title'] == 'Title 1'
    assert organic_results[0]['url'] == 'https://example.com/1'
    assert organic_results[0]['snippet'] == 'snippet 1'
    assert organic_results[0]['rich_snippet'] == 'rich snippet 1'
    assert organic_results[1]['title'] == 'Title 2'
    assert organic_results[1]['url'] == 'https://example.com/2'
    assert organic_results[1]['snippet'] == 'snippet 2'
    assert organic_results[1]['rich_snippet'] == ''


def test_get_organic_no_results():
    """Checks that _get_organic returns an empty list when no results are found."""
    parser = GoogleHtmlParser("<html><body></body></html>", user_agent='desktop')
    organic_results = parser._get_organic()
    assert organic_results == []


def test_get_featured_snippet(mock_html_desktop):
    """Checks that _get_featured_snippet returns the featured snippet correctly."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    featured_snippet = parser._get_featured_snippet()
    assert featured_snippet['title'] == 'Featured Snippet Title'
    assert featured_snippet['url'] == 'https://example.com/featured'


def test_get_featured_snippet_not_found():
    """Checks that _get_featured_snippet returns None when not found."""
    parser = GoogleHtmlParser("<html><body></body></html>", user_agent='desktop')
    featured_snippet = parser._get_featured_snippet()
    assert featured_snippet is None


def test_get_knowledge_card(mock_html_desktop):
    """Checks that _get_knowledge_card returns the knowledge card correctly."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    knowledge_card = parser._get_knowledge_card()
    assert knowledge_card['title'] == 'Knowledge Card Title'
    assert knowledge_card['subtitle'] == 'Knowledge Card Subtitle'
    assert knowledge_card['description'] == 'Knowledge Card Description'
    assert len(knowledge_card['more_info']) == 2
    assert knowledge_card['more_info'][0] == {'key1': 'Value1'}
    assert knowledge_card['more_info'][1] == {'key2': 'Value2'}


def test_get_knowledge_card_not_found():
    """Checks that _get_knowledge_card returns None when not found."""
    parser = GoogleHtmlParser("<html><body></body></html>", user_agent='desktop')
    knowledge_card = parser._get_knowledge_card()
    assert knowledge_card is None


def test_get_scrolling_sections(mock_html_desktop):
    """Checks that _get_scrolling_sections returns scrolling sections data correctly."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    scrolling_sections = parser._get_scrolling_sections()
    assert len(scrolling_sections) == 1
    assert scrolling_sections[0]['section_title'] == 'Top Stories'
    assert len(scrolling_sections[0]['section_data']) == 2
    assert scrolling_sections[0]['section_data'][0]['title'] == 'Top Story Title 1'
    assert scrolling_sections[0]['section_data'][0]['url'] == 'https://example.com/top_story1'
    assert scrolling_sections[0]['section_data'][1]['title'] == 'Top Story Title 2'
    assert scrolling_sections[0]['section_data'][1]['url'] == 'https://example.com/top_story2'


def test_get_scrolling_sections_no_sections():
     """Checks that _get_scrolling_sections returns an empty list when no sections are found."""
     parser = GoogleHtmlParser("<html><body></body></html>", user_agent='desktop')
     scrolling_sections = parser._get_scrolling_sections()
     assert scrolling_sections == []


def test_get_data_desktop(mock_html_desktop):
    """Checks that get_data returns the correct structure for desktop."""
    parser = GoogleHtmlParser(mock_html_desktop, user_agent='desktop')
    data = parser.get_data()
    assert 'estimated_results' in data
    assert 'featured_snippet' in data
    assert 'knowledge_card' in data
    assert 'organic_results' in data
    assert 'scrolling_widgets' in data
    assert data['estimated_results'] == 1234567
    assert data['featured_snippet']['title'] == 'Featured Snippet Title'
    assert data['knowledge_card']['title'] == 'Knowledge Card Title'
    assert len(data['organic_results']) == 2
    assert len(data['scrolling_widgets']) == 1


def test_get_data_mobile(mock_html_mobile):
    """Checks that get_data returns an empty dict for mobile user agent."""
    parser = GoogleHtmlParser(mock_html_mobile, user_agent='mobile')
    data = parser.get_data()
    assert data == {}
```