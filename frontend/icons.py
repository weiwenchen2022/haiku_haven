from enum import StrEnum


class Icons(StrEnum):
    LOGIN = ":material/login:"
    SIGNUP = ":material/person_add:"
    HOME = ":material/home:"
    LOGOUT = ":material/logout:"
    ADD = ":material/add_circle:"
    CALENDAR = ":material/calendar_month:"
    CLOCK = ":material/schedule:"
    EDIT = ":material/edit:"
    DELETE = ":material/delete:"

    def __str__(self) -> str:
        return self.value
