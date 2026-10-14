"""S14 - Buzz (TC-BUZZ-01 s/d TC-BUZZ-04)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
import time
from pages.buzz_page import BuzzPage


def test_tc_buzz_01_halaman_buzz_newsfeed(logged_in):
    """TC-BUZZ-01: Halaman Buzz Newsfeed terbuka."""
    buzz = BuzzPage(logged_in)
    buzz.open("/buzz/viewBuzz")
    buzz.wait_breadcrumb()
    assert "/buzz/viewBuzz" in logged_in.current_url


def test_tc_buzz_02_kotak_post_dan_tombol_post_tampil(logged_in):
    """TC-BUZZ-02: Kotak post dan tombol Post tampil."""
    buzz = BuzzPage(logged_in)
    buzz.open("/buzz/viewBuzz")
    assert buzz.is_visible(BuzzPage.POST_BOX)
    assert buzz.is_visible(BuzzPage.BUTTON_POST)


def test_tc_buzz_03_buat_post_baru(logged_in):
    """TC-BUZZ-03: Buat post baru di newsfeed."""
    buzz = BuzzPage(logged_in)
    text = f"Tugas 4 Selenium Test {int(time.time())}"
    buzz.create_post(text)
    assert buzz.wait_post_visible(text) is not None


def test_tc_buzz_04_filter_most_liked_posts(logged_in):
    """TC-BUZZ-04: Filter Most Liked Posts."""
    buzz = BuzzPage(logged_in)
    buzz.open("/buzz/viewBuzz")
    buzz.click(BuzzPage.BUTTON_MOST_LIKED)
    assert buzz.is_visible(BuzzPage.POST_BOX)
