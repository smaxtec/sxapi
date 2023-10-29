from sxapi.base import (
    ApiTypes,
    BaseAPI,
)
from sxapi.publicV2.alarms import Alarms
from sxapi.publicV2.data import Data
from sxapi.publicV2.feedrations import Feedrations
from sxapi.publicV2.groups import Groups
from sxapi.publicV2.todos import Todos
from sxapi.publicV2.users import Users
from sxapi.publicV2.events import Events
from sxapi.publicV2.animalgroups import AnimalGroups
from sxapi.publicV2.notes import Notes

PUBLIC_API_V2_BASE_URL = "https://api.smaxtec.com/api/v2"


class PublicAPIV2(BaseAPI):
    def __init__(self, base_url=None, email=None, password=None, api_token=None):
        """Initialize a new public api client instance."""
        base_url = base_url or PUBLIC_API_V2_BASE_URL
        api_type = ApiTypes.PUBLIC

        self.todos = Todos(api=self)
        self.users = Users(api=self)
        self.alarms = Alarms(api=self)
        self.data = Data(api=self)
        self.groups = Groups(api=self)
        self.feedrations = Feedrations(api=self)
        self.events = Events(api=self)
        self.animalgroups = AnimalGroups(api=self)
        self.notes = Notes(api=self)

        super().__init__(
            base_url,
            email=email,
            password=password,
            api_token=api_token,
            api_type=api_type,
        )
