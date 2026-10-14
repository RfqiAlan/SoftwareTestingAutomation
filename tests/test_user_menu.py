"""S15 - Menu User & Akun (TC-USER-01 s/d TC-USER-05)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from pages.main_page import MainPage


def test_tc_user_01_dropdown_user_berisi_menu_lengkap(logged_in):
    """TC-USER-01: Dropdown user berisi menu lengkap (About, Support, Change Password, Logout)."""
    main = MainPage(logged_in)
    main.open_user_menu()
    assert main.is_visible(main._menu_item(1))  # About
    assert main.is_visible(main._menu_item(2))  # Support
    assert main.is_visible(main._menu_item(3))  # Change Password
    assert main.is_visible(main._menu_item(4))  # Logout


def test_tc_user_02_dialog_about(logged_in):
    """TC-USER-02: Dialog About dapat dibuka dan ditutup."""
    main = MainPage(logged_in)
    dialog = main.open_about()
    assert dialog.is_displayed()
    main.close_about()


def test_tc_user_03_halaman_support(logged_in):
    """TC-USER-03: Halaman Support terbuka."""
    main = MainPage(logged_in)
    main.open_support()
    main.wait_url_contains("/help/support")
    assert "/help/support" in logged_in.current_url


def test_tc_user_04_halaman_change_password(logged_in):
    """TC-USER-04: Halaman Change Password terbuka."""
    main = MainPage(logged_in)
    main.open_change_password()
    main.wait_url_contains("/pim/updatePassword")
    assert "/pim/updatePassword" in logged_in.current_url


def test_tc_user_05_change_password_semua_kolom_kosong(logged_in):
    """TC-USER-05: Change Password - semua kolom kosong."""
    main = MainPage(logged_in)
    main.open("/pim/updatePassword")
    main.click(MainPage.SUBMIT)
    assert main.wait_error_count(1) >= 1
