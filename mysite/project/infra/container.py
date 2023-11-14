from dependency_injector import containers, providers
from apps.account.infra.container import AccountContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "apps.account.presentation.api",
        ]
    )

    account = providers.Container(AccountContainer)