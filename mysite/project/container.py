from dependency_injector import containers, providers

from apps.users.container import UserContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "apps.users.api",
            # "reception.presentation.rest.api"
        ]
    )

    user = providers.Container(UserContainer)