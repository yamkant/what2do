from dependency_injector import containers, providers

from apps.todo.container import TodoContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "apps.todo.api",
        ]
    )

    todo = providers.Container(TodoContainer)
