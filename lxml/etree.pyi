# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

import typing
from typing import Any, Dict, List, MutableMapping, Tuple, Union, Optional
from typing import Iterable, Iterator, SupportsBytes


# We do *not* want `typing.AnyStr` because it is a `TypeVar`, which is an
# unnecessary constraint. It seems reasonable to constrain each
# List/Dict argument to use one type consistently, though, and it is
# necessary in order to keep these brief.
_AnyStr = Union[str, bytes]
_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]


class ElementChildIterator(Iterator['Element']):
    def __iter__(self) -> 'ElementChildIterator': ...
    def __next__(self) -> 'Element': ...

class Element(Iterable['Element']):
    def addprevious(self, element: 'Element') -> None: ...
    def addnext(self, element: 'Element') -> None: ...
    def clear(self) -> None: ...
    def get(self, key: _AnyStr, default: Optional[_AnyStr] = ...) -> _AnyStr: ...
    def xpath(self, _path: _AnyStr, namespaces: Optional[_DictAnyStr] = ..., extensions: Any = ..., smart_strings: bool = ..., **_variables: Any) -> Any: ...
    # indeed returns a Union[bool, float, _AnyStr, List[Union[ElementBase, _AnyStr, Tuple[]]]]: ...
    # http://lxml.de/xpathxslt.html#xpath-return-values
    attrib = ...  # type: MutableMapping[str, str]
    text = ...  # type: str
    tag = ...  # type: str
    def append(self, element: 'Element') -> 'Element': ...
    def __iter__(self) -> ElementChildIterator: ...

    def __init__(self, _tag: _AnyStr, attrib: _DictAnyStr = ..., nsmap: _DictAnyStr = ..., **extra: _AnyStr) -> None: ...

    def find(self, _name: _AnyStr, namespaces: Optional[_DictAnyStr] = ...) -> Element: ...
    def findall(self, _name: _AnyStr, namespaces: Optional[_DictAnyStr] = ...) -> List[Element]: ...

class ElementBase(Element): ...

class _ElementTree:
    def write(self,
              file: Union[_AnyStr, typing.IO],
              encoding: _AnyStr = ...,
              method: _AnyStr = ...,
              pretty_print: bool = ...,
              xml_declaration: Any = ...,
              with_tail: Any = ...,
              standalone: bool = ...,
              compression: int = ...,
              exclusive: bool = ...,
              with_comments: bool = ...,
              inclusive_ns_prefixes: _ListAnyStr = ...) -> None: ...
    def xpath(self, _path: _AnyStr, namespaces: Optional[_DictAnyStr] = ..., extensions: Any = ..., smart_strings: bool = ..., **_variables: Any) -> Any: ...

class _XSLTQuotedStringParam: ...

class XMLParser:
    def __init__(self, schema: Any = ...) -> None: ...

class XMLSchema:
    def __init__(self,
                 etree: Union[Element, _ElementTree] = ...,
                 file: Union[_AnyStr, typing.IO] = ...) -> None: ...
    def assertValid(self, etree: Union[Element, _ElementTree]) -> None: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(self,
                 xslt_input: Union[Element, _ElementTree],
                 extensions: _Dict_Tuple2AnyStr_Any = ...,
                 regexp: bool = ...,
                 access_control: XSLTAccessControl = ...) -> None: ...
    def __call__(self,
                 _input: Union[Element, _ElementTree],
                 profile_run: bool = ...,
                 **kwargs: Union[_AnyStr, _XSLTQuotedStringParam]) -> Any: ...
    @staticmethod
    def strparam(s: _AnyStr) -> _XSLTQuotedStringParam: ...

def SubElement(_parent: Element, _tag: _AnyStr,
               attrib: _DictAnyStr = ...,
               nsmap: _DictAnyStr = ...,
               **extra: _AnyStr) -> Element: ...
def ElementTree(element: Element = ...,
                file: Union[_AnyStr, typing.IO] = ...,
                parser: XMLParser = ...) -> _ElementTree: ...
def ProcessingInstruction(target: _AnyStr, text: _AnyStr = ...) -> Element: ...
def parse(source: Union[_AnyStr, typing.IO],
          parser: XMLParser = ...,
          base_url: _AnyStr = ...) -> _ElementTree: ...
def fromstring(text: _AnyStr,
               parser: XMLParser = ...,
               *,
               base_url: _AnyStr = ...) -> Element: ...
def tostring(element_or_tree: Union[Element, _ElementTree],
             encoding: Union[str, type] = ...,
             method: str = ...,
             xml_declaration: bool = ...,
             pretty_print: bool = ...,
             with_tail: bool = ...,
             standalone: bool = ...,
             doctype: str = ...,
             exclusive: bool = ...,
             with_comments: bool = ...,
             inclusive_ns_prefixes: Any = ...) -> _AnyStr: ...

class _ErrorLog: ...

class Error(Exception): ...

class LxmlError(Error):
    def __init__(self, message: Any, error_log: _ErrorLog = ...) -> None: ...
    error_log = ...  # type: _ErrorLog

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...
class ParseError(LxmlSyntaxError): ...
class XMLSyntaxError(ParseError): ...

class _Validator: ...

class DTD(_Validator):
    def __init__(self,
                 file: Union[_AnyStr, typing.IO] = ...,
                 *,
                 external_id: Any = ...) -> None: ...

    def assertValid(self, etree: Element) -> None: ...
