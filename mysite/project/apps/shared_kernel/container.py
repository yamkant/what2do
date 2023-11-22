from dependency_injector import containers, providers

from apps.todo.container import TodoContainer
from apps.user.container import UserContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "apps.user.api",
            "apps.todo.api",
        ]
    )

    user = providers.Container(UserContainer)
    todo = providers.Container(TodoContainer)
