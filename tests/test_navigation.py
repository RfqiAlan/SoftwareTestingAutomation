"""S10 - Dashboard & Navigasi Menu
Diadaptasi dari Tugas3_OrangeHRM.side
"""
import pytest
from selenium.webdriver.common.by import By

from pages.main_page import MainPage


@pytest.mark.smoke
def test_tc_dash_01_widget_dashboard_tampil(logged_in):
    """TC-DASH-01: Widget dashboard tampil."""
    main = MainPage(logged_in)
    assert main.dashboard_widget_count() >= 1


def test_tc_dash_02_pencarian_menu_sidebar_ada_hasil(logged_in):
    """TC-DASH-02: Pencarian menu sidebar - ada hasil."""
    main = MainPage(logged_in)
    main.search_sidebar("Leave")
    leave_item = main.visible((By.XPATH, "//a[contains(@class,'oxd-main-menu-item')][contains(@href,'/leave/') or .//span[text()='Leave']]"))
    assert leave_item.is_displayed()
    admin_items = logged_in.find_elements(By.XPATH, "//a[contains(@class,'oxd-main-menu-item')][contains(@href,'/admin/') or .//span[text()='Admin']]")
    assert not any(item.is_displayed() for item in admin_items)


def test_tc_dash_03_pencarian_menu_sidebar_tidak_ada_hasil(logged_in):
    """TC-DASH-03: Pencarian menu sidebar - tidak ada hasil."""
    main = MainPage(logged_in)
    main.search_sidebar("zzzzzz")
    assert len(main.get_visible_menu_items()) == 0


def test_tc_nav_08_menu_dashboard(logged_in):
    """TC-NAV-08: Menu Dashboard membuka halaman Dashboard."""
    main = MainPage(logged_in)
    main.open_module("/dashboard/index")
    assert "/dashboard/index" in logged_in.current_url


def test_tc_nav_09_menu_directory(logged_in):
    """TC-NAV-09: Menu Directory membuka halaman modul Directory."""
    main = MainPage(logged_in)
    main.open_module("/directory/viewDirectory")
    assert "/directory/viewDirectory" in logged_in.current_url


def test_tc_nav_12_menu_buzz(logged_in):
    """TC-NAV-12: Menu Buzz membuka halaman modul Buzz."""
    main = MainPage(logged_in)
    main.open_module("/buzz/viewBuzz")
    assert "/buzz/viewBuzz" in logged_in.current_url


# Alias kompatibilitas
test_dashboard_menampilkan_widget = test_tc_dash_01_widget_dashboard_tampil
