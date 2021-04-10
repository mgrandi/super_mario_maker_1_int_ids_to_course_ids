import attr


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MarioMakerOneCourseID:
    integer_id:int = attr.ib()
    one:str = attr.ib()
    two:str = attr.ib()
    three:str = attr.ib()
    four:str = attr.ib()


    def as_course_id_str(self):
        return f"SMM1::{self.integer_id}::{self.one}-{self.two}-{self.three}-{self.four}"