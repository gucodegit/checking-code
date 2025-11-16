from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls) -> str:
        name = cls.__name__
        chars = []
        for c_idx, char in enumerate(name):
            if c_idx and char.isupper():
                nxt_idx = c_idx + 1
                flag = nxt_idx >= len(name) or name[nxt_idx].isupper()
                prev_char = name[c_idx - 1]
                if prev_char.isupper() and flag:
                    pass
                else:
                    chars.append("_")
            chars.append(char.lower())
        return "".join(chars)
