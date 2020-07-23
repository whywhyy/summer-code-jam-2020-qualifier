"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re
from itertools import count

class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self._field_type = field_type
      # self.attribute_name = None
    """정답코드
    class에 대한 descriptor 을 생성하였다.
    def __repr__(self) -> str:
        # Return the 'official' string representation of the descriptor.
        cls_name = self.__class__.__name__
        return f"<{cls_name} descriptor with field_type={self.field_type!r}>"
    """

    """정답코드
    # __set_name__ 을 정의 하였다.
    # alias 를 가능하게 한다..
    def __set_name__(self, owner: typing.Type[typing.Any], name: str) -> None:
        # Capture the fully qualified name assigned to the descriptor instance.
        # As Python allows you to alias the descriptor instance by assigning another
        # class attribute to the descriptor instance, we only capture the name the
        # first time `__set_name__` runs.
        # This is similar to what happens when creating function objects: The `__name__`
        # attribute of the function object is only assigned when the function object is
        # first created. Subsequent aliasing of the function by assigning another name
        # to it does not change the `__name__` attribute.
        # >>> def foo(): pass
        # >>> foo.__name__
        # 'foo'
        # >>> bar = foo
        # >>> bar.__name__
        # 'foo'
        if self.attribute_name is None:
            self.attribute_name = name
    """
    def __set__(self, obj, val):
        if type(val) == str:
          raise TypeError("""expected an instance of type 'int' for attribute 'attribute', got 'str' instead""")
        obj._field_type = val
    """
    def __set__(self, obj: typing.Optional[AnyType], new_value: typing.Any) -> None:
        # isinstance 로 동일한 타입인지 확인한다!
        # 다르면 typeError 출력! 오홓!
        # 그리고 해당객체의 내부 파라미터접근시 
        # obj.__dict__[self.attribute_name] = new_value
        # __dict__ 로 내부속성 접하여, None 에 new_vale 를 넣는듯하다!?
        if not isinstance(new_value, self.field_type):
            # Get the names of the expected type and the actual type of the new_value
            expected_type = self.field_type.__name__
            actual_type = type(new_value).__name__

            # Raise a type error to indicate that actual type did not validate.
            raise TypeError(
                f"expected an instance of type {expected_type!r} for attribute "
                f"{self.attribute_name!r}, got {actual_type!r} instead."
            )

        obj.__dict__[self.attribute_name] = new_value
    """

    def __get__(self, obj, val):
        return obj._field_type

    """'
    # 에러처리가 되어있다.
    # KeyError 시 해당 attrivute 가 없다고 잘 나온다(?)
    def __get__(self, obj: typing.Optional[AnyType], owner: typing.Type[AnyType]) -> typing.Any:
        # If the attribute is accessed via the `owner` class object, we return
        # the descriptor itself. This allows for easier introspection of the
        # descriptor.
        if obj is None:
            return self

        # Try to get the actual value from `obj.__dict__`. Since this raises
        # a KeyError, not an AttributeError, when no value was set yet, we
        # catch the exception and raise an AttributeError instead.
        try:
            value = obj.__dict__[self.attribute_name]
        except KeyError:
            cls_name = owner.__name__
            raise AttributeError(
                f"{cls_name!r} object has no attribute {self.attribute_name!r}"
            ) from None

        return value
    """


class Article:
    """The `Article` class you need to write for the qualifier."""
    
    _ids = count(0)

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self._title = title
        self._author = author
        self._publication_date=publication_date
        self._content = content
        self._id = next(self._ids)
        self._last_edited = None

    @property
    def last_edited (self):
        return self._last_edited 

    @last_edited .setter
    def last_edited (self, value: datetime.datetime):
        self._last_edited  = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publication_date(self):
        return self._publication_date

    @publication_date.setter
    def publication_date(self, value):
        self._publication_date = value

    @property
    def content(self):
      # def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value):
      # def content(self, new_content: str) -> None:
        self.last_edited = datetime.datetime.now()
        self._content = value

    def __repr__(self):
      """정답코드
      # def __repr__(self) -> str: typehint 를 작성하였다!
      # cls = self.__class__.__name__
      # 정답코드에서는 {cls} 로 접근하여 작성한다.
      # 어떤 장점이 있는지 모르겠다 ㅠㅠ
      """
      return (f'<{self.__class__.__name__}'
              f' title={self.title!r}'
              f' author={self.author!r}'
              f' publication_date={self.publication_date.isoformat()!r}>')
  
    def __len__(self):
      return len(self.content)

    def short_introduction(self, n_characters:int):
      """정답코드
      # def short_introduction(self, n_characters: int) -> str:
      # typeHint!
      # 일단 짧으면 바로 리턴!
      # 해당 길이만큼 cut!
      # " ", "\n" 가장 큰거 찾기 !
      # max 값 separator 로 !! 그리고 다시 Cut ! 깔끔하다!.
      # 
      # 내코드는 기존 "\n" 를 " " 로 다 바꿔버려서 
      # 문제가 내 정답은 틀린듯하다.!
      if len(self._content) <= n_characters:
            return self._content
      short_content = self._content[:n_characters + 1]
      rightmost_space = short_content.rfind(" ")
      rightmost_newline = short_content.rfind("\n")
      rightmost_separator = max((rightmost_space, rightmost_newline))
      return short_content[:rightmost_separator]
      """

      ret_list = []
      content = self.content
      content = content.split()
      total_len = 0
      for i in content:
        total_len += len(i)
        if n_characters >= total_len:
          ret_list.append(i)
        else:
          break
        total_len+=1
      return " ".join(ret_list)

      
      
    def most_common_words(self,n:int):
      """정답코드
      # def most_common_words(self, n_words: int) -> typing.Dict[str, int]:
      # type hint!! dict[str,int] 로 구현
      # lowercase_content = self._content.lower()
      # if - for 문 으로 list 생성 후 .join 한다!
      clean_content = "".join(
          char if char in string.ascii_lowercase else " "
          for char in lowercase_content
      )
      words = clean_content.split()
      # Counter  most_common 으로 상위 n_word 만큼만 reurn함.
      # ordered 하게 return 하는 특징이 있다!
      word_counts = collections.Counter(words)
      most_common_words = dict(word_counts.most_common(n_words))
      return most_common_words
      """
      result = {}
      if n == 0 :
        return result
      content = self.content
      word_list = re.split('\W', content)
      word_list = ' '.join(word_list).split()
      word_list = list(map(lambda x:x.lower(),word_list))

      cal_dict = {}
      for idx,val in enumerate(word_list):
        try:
          cal_dict[val]["count"] += 1
        except KeyError:
          cal_dict[val] = {"count":1,"idx":idx}
      
      # dict to list
      cal_dict = sorted(cal_dict.items(), key=lambda x: (x[1]["idx"]))
      # list
      cal_dict = sorted(cal_dict, key=lambda x: (x[1]["count"]), reverse=True)

 
      count = 0
      for i in cal_dict:
        count+=1 
        if count > n :
          break
        result[i[0]] = i[1]["count"]
          
      return result
      
    def __lt__(self, other):
      return self.publication_date < other.publication_date
    """정답코드
    #  def __lt__(self, other: Article) -> typing.Union[bool, NotImplemented]:
    # 동일한 Class 이름인지 확인하여 진행!
    # if not isinstance(other, Article):
    #         return NotImplemented
    # reverse 의 경우 __gt__ 를 사용한다는건 방금 암!
    """
