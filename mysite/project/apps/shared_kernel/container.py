from dependency_injector import containers, providers

from apps.user.container import UserContainer
from apps.todo.container import TodoContainer
from apps.news.container import PostContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "apps.user.api",
            "apps.todo.api",
            "apps.news.api",
        ]
    )

    user = providers.Container(UserContainer)
    todo = providers.Container(TodoContainer)
    post = providers.Container(PostContainer)
