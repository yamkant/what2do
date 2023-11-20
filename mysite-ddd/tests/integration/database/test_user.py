from apps.account.domain.entity.user import User


def test_새로운_유저를_등록합니다(test_session):
    # given
    new_user = User(email="dev.yamkim@example.com", hash_passsword="5933", is_active=True)

    # when
    test_session.add(new_user)
    test_session.commit()

    # then
    assert new_user == test_session.query(User).filter(
        User.email == new_user.email
    ).first()
