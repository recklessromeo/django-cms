from django.conf import settings
from cms.utils import cms_static_url

# Uses TinyMCE as editor (no inline plugins). Requires django-tinymce app. 
# If false, then WYMEditor is used. 
USE_TINYMCE = getattr(settings, 'CMS_USE_TINYMCE', "tinymce" in settings.INSTALLED_APPS)
USE_IMPERAVI = getattr(settings, 'CMS_USE_IMPERAVI', "imperavi" in settings.INSTALLED_APPS)#dm
USE_CKEDITOR = getattr(settings, 'CMS_USE_CKEDITOR', "ckeditor" in settings.INSTALLED_APPS)

if USE_TINYMCE:
    import tinymce.settings
    TINYMCE_CONFIG = getattr(settings, 'CMS_PLUGIN_TEXT_TINYMCE_CONFIG', tinymce.settings.DEFAULT_CONFIG)
#dm
if USE_CKEDITOR:
    CKEDITOR_CONFIG = getattr(settings, 'CMS_PLUGIN_TEXT_CKEDITOR_CONFIG', {})

WYM_TOOLS = ",\n".join([
    "{'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'}",
    "{'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'}",
    "{'name': 'Superscript', 'title': 'Superscript', 'css': 'wym_tools_superscript'}",
    "{'name': 'Subscript', 'title': 'Subscript', 'css': 'wym_tools_subscript'}",
    "{'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'}",
    "{'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'}",
    "{'name': 'Indent', 'title': 'Indent', 'css': 'wym_tools_indent'}",
    "{'name': 'Outdent', 'title': 'Outdent', 'css': 'wym_tools_outdent'}",
    "{'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'}",
    "{'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'}",
    "{'name': 'Paste', 'title': 'Paste_From_Word', 'css': 'wym_tools_paste'}",
    "{'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'}",
    #"{'name': 'CreateLink', 'title': 'Link', 'css': 'wym_tools_link'}",
    #"{'name': 'Unlink', 'title': 'Unlink', 'css': 'wym_tools_unlink'}",
    #"{'name': 'InsertImage', 'title': 'Image', 'css': 'wym_tools_image'}",
    #"{'name': 'InsertTable', 'title': 'Table', 'css': 'wym_tools_table'}",
    #"{'name': 'Preview', 'title': 'Preview', 'css': 'wym_tools_preview'}",
])

WYM_TOOLS = getattr(settings, "WYM_TOOLS", WYM_TOOLS)

WYM_CONTAINERS = ",\n".join([
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}",
    "{'name': 'H1', 'title': 'Heading_1', 'css': 'wym_containers_h1'}",
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}",
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}",
    "{'name': 'H4', 'title': 'Heading_4', 'css': 'wym_containers_h4'}",
    "{'name': 'H5', 'title': 'Heading_5', 'css': 'wym_containers_h5'}",
    "{'name': 'H6', 'title': 'Heading_6', 'css': 'wym_containers_h6'}",
    "{'name': 'PRE', 'title': 'Preformatted', 'css': 'wym_containers_pre'}",
    "{'name': 'BLOCKQUOTE', 'title': 'Blockquote', 'css': 'wym_containers_blockquote'}",
    "{'name': 'TH', 'title': 'Table_Header', 'css': 'wym_containers_th'}",
    "{'name': 'READMORE', 'title': 'Read_More', 'css': 'wym_containers_pre'}",#dm
])
    
WYM_CONTAINERS = getattr(settings, "WYM_CONTAINERS", WYM_CONTAINERS)

WYM_CLASSES = ",\n".join([
    "{'name': 'date', 'title': 'PARA: Date', 'expr': 'p'}",
    "{'name': 'hidden-note', 'title': 'PARA: Hidden note', 'expr': 'p[@class!=\"important\"]'}",
    "{'name': 'justify', 'title': 'PARA: Justify', 'expr': 'p' }",#dm
    "{'name': 'underline', 'title': 'PARA: Undeline', 'expr': 'p' }",
    "{'name': 'highlight', 'title': 'PARA: Highlight', 'expr': '*'}",
    "{'name': 'center', 'title': 'PARA: Center', 'expr': '*'}",
    "{name: 'text-align', rules:['left', 'center', 'right', 'justify'], join: '-'}"
])
    
WYM_STYLES = ",\n".join([
    "{'name': '.hidden-note', 'css': 'color: #999; border: 2px solid #ccc;'}",
    "{'name': '.date', 'css': 'background-color: #ff9; border: 2px solid #ee9;'}",
    "{'name': '.justify', 'css': 'text-align: justify ;' }",#dm
    "{'name': '.undeline', 'css': 'text-decoration: underline;' }",
    "{'name': '.center', 'css': 'text-align: center ;' }",
    "{'name': '.highlight', 'css': 'background-color: yellow ;'}",
])

WYM_CLASSES = getattr(settings, "WYM_CLASSES", WYM_CLASSES)
WYM_STYLES = getattr(settings, "WYM_STYLES", WYM_STYLES)

#Advantageously replaces WYM_CLASSES and WYM_STYLES
##Prepare url for wymeditor.css
WYM_STYLESHEET = getattr(settings, "WYM_STYLESHEET",  '"%s"' % cms_static_url('css/wymeditor.css'))
