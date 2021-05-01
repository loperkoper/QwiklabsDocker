from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from time import sleep
import random
sleep(5)

def terminal():
    
    ##select terminal
    mouse.position = (10, 712)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (58, 491)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (251, 519)
    mouse.click(Button.left, 1)
    sleep(1.5)
    ##select on terminal
    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(1)

def first_change_ip():

    ##select zenmate
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(4)
    ##click 4 times to start
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(3)
    ##change to usa
    mouse.position = (1137, 528)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1023, 346)
    mouse.click(Button.left, 1)
    sleep(1)
    ##click to close it
    mouse.position = (1307, 63)
    mouse.click(Button.left, 1)
    sleep(1)
    
def change_ip():

    ##select zenmate
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(2)
    ##close add
    mouse.position = (1147, 605)
    mouse.click(Button.left, 1)
    sleep(2)
    ##stop
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(1.6)
    ##start
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(1.6)
    ##click to close it
    mouse.position = (1307, 63)
    mouse.click(Button.left, 1)
    sleep(1)
    
def on_off_ip():

    ##select zenmate
    mouse.position = (1306, 70)
    mouse.click(Button.left, 1)
    sleep(2)
    ##close add
    mouse.position = (1147, 605)
    mouse.click(Button.left, 1)
    sleep(2)
    ##start
    mouse.position = (1140, 368)
    mouse.click(Button.left, 1)
    sleep(1.6)
    ##click to close it
    mouse.position = (1307, 63)
    mouse.click(Button.left, 1)
    sleep(1)


##minimize Terminal
mouse.position = (968, 94)
mouse.click(Button.left, 1) 
sleep(1)

terminal()

##write command
keyboard.type('firefox')
sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(10)

##close second page
mouse.position = (434, 35)
mouse.click(Button.left, 1)
sleep(1)

##click on searchbar
keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release(Key.ctrl)
keyboard.release('l')
sleep(0.5)

##go to solver site
keyboard.type('https://addons.mozilla.org/en-US/firefox/addon/buster-captcha-solver/')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(7)

##click on add to firefox
mouse.position = (734, 482)
mouse.click(Button.left, 1) 
sleep(4)
mouse.position = (643, 299)
mouse.click(Button.left, 1)
sleep(2)

##new tab
mouse.position = (240, 32)
mouse.click(Button.left, 1)
sleep(3)

## close pre page
mouse.position = (208, 34)
mouse.click(Button.left, 1)
sleep(2)

##click on searchbar
keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release(Key.ctrl)
keyboard.release('l')
sleep(0.5)

##go to vpn site
keyboard.type('https://addons.mozilla.org/en-US/firefox/addon/zenmate-free-vpn-best/')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(7)

##click on add to firefox
mouse.position = (741, 513)
mouse.click(Button.left, 1) 
sleep(4)
mouse.position = (594, 354)
mouse.click(Button.left, 1)
sleep(2)

##click on okay
mouse.position = (1345, 276)
mouse.click(Button.left, 1)
sleep(2)

##close vpn page
mouse.position = (433, 38)
mouse.click(Button.left, 1)
sleep(2)

##new tab
mouse.position = (240, 32)
mouse.click(Button.left, 1)
sleep(3)

##start vpn
first_change_ip()

## close pre page
mouse.position = (208, 34)
mouse.click(Button.left, 1)
sleep(2)


def signup():
    
    def terminal():
        
        ##select terminal
        mouse.position = (10, 712)
        mouse.click(Button.left, 1)
        sleep(1.5)
        mouse.position = (58, 491)
        mouse.click(Button.left, 1)
        sleep(1.5)
        mouse.position = (251, 519)
        mouse.click(Button.left, 1)
        sleep(1.5)
        ##select on terminal
        mouse.position = (570, 408)
        mouse.click(Button.left, 1)
        sleep(1)

    def first_change_ip():

        ##select zenmate
        mouse.position = (1306, 70)
        mouse.click(Button.left, 1)
        sleep(4)
        ##click 4 times to start
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(3)
        ##change to usa
        mouse.position = (1137, 528)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1023, 346)
        mouse.click(Button.left, 1)
        sleep(1)
        ##click to close it
        mouse.position = (1307, 63)
        mouse.click(Button.left, 1)
        sleep(1)
        
    def change_ip():

        ##select zenmate
        mouse.position = (1306, 70)
        mouse.click(Button.left, 1)
        sleep(2)
        ##close add
        mouse.position = (1147, 605)
        mouse.click(Button.left, 1)
        sleep(2)
        ##stop
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1.6)
        ##start
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1.6)
        ##click to close it
        mouse.position = (1307, 63)
        mouse.click(Button.left, 1)
        sleep(1)
        
    def on_off_ip():

        ##select zenmate
        mouse.position = (1306, 70)
        mouse.click(Button.left, 1)
        sleep(2)
        ##close add
        mouse.position = (1147, 605)
        mouse.click(Button.left, 1)
        sleep(2)
        ##start
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1.6)
        ##click to close it
        mouse.position = (1307, 63)
        mouse.click(Button.left, 1)
        sleep(1)
        
    def error1():
        ##click on retry
        mouse.position = (872, 349)
        mouse.click(Button.left, 1)
        sleep(1)
        ##click on recaptcha
        mouse.position = (471, 316)
        mouse.click(Button.left, 1)
        sleep(3)

    ##click on searchbar
    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release(Key.ctrl)
    keyboard.release('l')
    sleep(0.5)
        
    ##go to qwiklabs signup
    keyboard.type('https://www.qwiklabs.com/users/sign_up')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.5)
    ##new tab
    mouse.position = (240, 35)
    mouse.click(Button.left, 1)
    sleep(1)
    ##go to email generator
    keyboard.type('https://generator.email/')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)
    ##close add
    mouse.position = (1309, 484)
    mouse.click(Button.left, 1)
    sleep(3)
    ##copy email
    mouse.position = (998, 565)
    mouse.click(Button.left, 2)
    sleep(1)
    mouse.position = (1000, 485)
    mouse.click(Button.left, 2)
    sleep(1)
    ##go to first page
    mouse.position = (96, 32)
    mouse.click(Button.left, 1)
    sleep(1)
    ##click on name
    mouse.position = (539, 417)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.type('alex')
    ##click on last name
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.5)
    keyboard.type('brown')
    ##click on email
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    sleep(0.5)
    ##click on company
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.5)
    keyboard.type('boboltala')
    ##click on pass
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.5)
    keyboard.type('boboltala1$$')
    sleep(0.5)
    ##click on pass
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.5)
    keyboard.type('boboltala1$$')
    sleep(0.5)
    ##scroll down
    mouse.position = (1360, 613)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1360, 613)
    mouse.click(Button.left, 1)
    sleep(1)
    ##click on recaptcha
    mouse.position = (431, 311)
    mouse.click(Button.left, 1)
    sleep(7)
    ##click on first solver
    mouse.position = (582, 589)
    mouse.click(Button.left, 1)
    sleep(7)
    ##def retry
    error1()
    ##click on refresh
    mouse.position = (486, 431)
    mouse.click(Button.left, 1)
    sleep(5)
    ##click on solver
    mouse.position = (580, 434)
    mouse.click(Button.left, 1)
    sleep(7)
    ##def retry
    error1()
    ##click on refresh
    mouse.position = (486, 431)
    mouse.click(Button.left, 1)
    sleep(5)
    ##click on solver
    mouse.position = (580, 434)
    mouse.click(Button.left, 1)
    sleep(7)
    ##def retry
    error1()
    ##click on refresh
    mouse.position = (486, 431)
    mouse.click(Button.left, 1)
    sleep(5)
    ##click on solver
    mouse.position = (580, 434)
    mouse.click(Button.left, 1)
    sleep(7)
    ##def retry
    error1()
    mouse.position = (582, 589)
    mouse.click(Button.left, 1)
    sleep(5)
    ##click on creat account
    mouse.position = (874, 464)
    mouse.click(Button.left, 1)
    sleep(1)
    ##go to second page
    mouse.position = (345, 30)
    mouse.click(Button.left, 1)
    sleep(5)
    ##refresh page
    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release(Key.ctrl)
    keyboard.release('r')
    sleep(7)
    ##close add
    mouse.position = (1309, 484)
    mouse.click(Button.left, 1)
    sleep(3)
    ##scroll down
    mouse.position = (1360, 616)
    mouse.click(Button.left, 1)
    sleep(1)
    ##click on confirm email
    mouse.position = (506, 128)
    mouse.click(Button.left, 1)
    sleep(10)
    mouse.position = (1309, 484)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##write pass
    mouse.position = (548, 416)
    mouse.click(Button.left, 1)
    sleep(0.5)
    keyboard.type('boboltala1$$')
    sleep(0.5)
    ##click on login
    mouse.position = (825, 558)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##close prepages
    mouse.position = (207, 34)
    mouse.click(Button.left, 1)
    sleep(2)
    mouse.position = (207, 34)
    mouse.click(Button.left, 1)
    sleep(2)
    ##back and refresh
    mouse.position = (19, 72)
    mouse.click(Button.left, 1)
    sleep(5)
    mouse.position = (52, 69)
    mouse.click(Button.left, 1)
    sleep(5)
    ##sleep
    sleep(10)
    ##click on search bar qwiklabs
    mouse.position = (823, 122)
    mouse.click(Button.left, 1)
    sleep(1)
    ##search a tour
    keyboard.type('A Tour of Qwiklabs and Google Cloud')
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)
    ##select on tour
    mouse.position = (254, 309)
    mouse.click(Button.left, 1)
    sleep(7)
    
def signin():
    
    def terminal():
        
        ##select terminal
        mouse.position = (10, 712)
        mouse.click(Button.left, 1)
        sleep(1.5)
        mouse.position = (58, 491)
        mouse.click(Button.left, 1)
        sleep(1.5)
        mouse.position = (251, 519)
        mouse.click(Button.left, 1)
        sleep(1.5)
        ##select on terminal
        mouse.position = (570, 408)
        mouse.click(Button.left, 1)
        sleep(1)

    def first_change_ip():

        ##select zenmate
        mouse.position = (1306, 70)
        mouse.click(Button.left, 1)
        sleep(4)
        ##click 4 times to start
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(3)
        ##change to usa
        mouse.position = (1137, 528)
        mouse.click(Button.left, 1)
        sleep(1)
        mouse.position = (1023, 346)
        mouse.click(Button.left, 1)
        sleep(1)
        ##click to close it
        mouse.position = (1307, 63)
        mouse.click(Button.left, 1)
        sleep(1)
        
    def change_ip():

        ##select zenmate
        mouse.position = (1306, 70)
        mouse.click(Button.left, 1)
        sleep(2)
        ##close add
        mouse.position = (1147, 605)
        mouse.click(Button.left, 1)
        sleep(2)
        ##stop
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1.6)
        ##start
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1.6)
        ##click to close it
        mouse.position = (1307, 63)
        mouse.click(Button.left, 1)
        sleep(1)
        
    def on_off_ip():

        ##select zenmate
        mouse.position = (1306, 70)
        mouse.click(Button.left, 1)
        sleep(2)
        ##close add
        mouse.position = (1147, 605)
        mouse.click(Button.left, 1)
        sleep(2)
        ##start
        mouse.position = (1140, 368)
        mouse.click(Button.left, 1)
        sleep(1.6)
        ##click to close it
        mouse.position = (1307, 63)
        mouse.click(Button.left, 1)
        sleep(1)

    ##select on start
    mouse.position = (92, 208)
    mouse.click(Button.left, 1)
    sleep(4)
    ##select recaptcha
    mouse.position = (54, 261)
    mouse.click(Button.left, 1)
    sleep(7)
    ##select solver
    mouse.position = (166, 594)
    mouse.click(Button.left, 1)
    sleep(7)
    ##refresh captcha
    ##select recaptcha
    mouse.position = (72, 351)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (73, 404)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(3)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click solver
    ##select recaptcha
    mouse.position = (165, 354)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (168, 406)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(5)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##refresh captcha
    ##select recaptcha
    mouse.position = (72, 351)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (73, 404)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(3)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click solver
    ##select recaptcha
    mouse.position = (165, 354)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (168, 406)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(5)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##refresh captcha
    ##select recaptcha
    mouse.position = (72, 351)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (73, 404)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(3)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click solver
    ##select recaptcha
    mouse.position = (165, 354)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (168, 406)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(5)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##refresh captcha
    ##select recaptcha
    mouse.position = (72, 351)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (73, 404)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(3)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click solver
    ##select recaptcha
    mouse.position = (165, 354)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (168, 406)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(5)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##refresh captcha
    ##select recaptcha
    mouse.position = (72, 351)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (73, 404)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(3)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click solver
    ##select recaptcha
    mouse.position = (165, 354)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (168, 406)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(5)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##refresh captcha
    ##select recaptcha
    mouse.position = (72, 351)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (73, 404)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(3)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)
    ##click solver
    ##select recaptcha
    mouse.position = (165, 354)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (168, 406)
    mouse.click(Button.left, 1)
    sleep(0.5)
    sleep(7)
    mouse.position = (55, 269)
    mouse.click(Button.left, 1)
    sleep(3)

    ##make vpn off
    on_off_ip()

    ##select consol
    mouse.position = (166, 352)
    mouse.click(Button.left, 1)
    sleep(1)
    ##go to first page
    mouse.position = (91, 37)
    mouse.click(Button.left, 1)
    sleep(1)
    ##copy username
    mouse.position = (243, 420)
    mouse.click(Button.left, 2)
    sleep(0.5)
    ##go to seconde page
    mouse.position = (317, 28)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##select to type email
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release(Key.ctrl)
    keyboard.release('a')
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    ##paste email
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.5)
    ##go to first page
    mouse.position = (91, 37)
    mouse.click(Button.left, 1)
    sleep(1)
    ##copy pass
    mouse.position = (242, 507)
    mouse.click(Button.left, 2)
    sleep(0.5)
    ##go to seconde page
    mouse.position = (317, 28)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##select to type pass
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release(Key.ctrl)
    keyboard.release('a')
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    ##paste pass
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(5)
    ##scroll down
    mouse.position = (1360, 614)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click on accept
    mouse.position = (593, 433)
    mouse.click(Button.left, 1)
    sleep(5)
    ##scroll down
    mouse.position = (1360, 614)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click on confirm
    mouse.position = (822, 542)
    mouse.click(Button.left, 1)
    sleep(15)
    ##click on checkbox
    mouse.position = (433, 447)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##click on agree and continue
    mouse.position = (869, 560)
    mouse.click(Button.left, 1)
    sleep(7)
    ##click on terminal
    mouse.position = (1168, 115)
    mouse.click(Button.left, 1)
    sleep(5)
    ##click on continue
    mouse.position = (545, 574)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.position = (407, 576)
    mouse.click(Button.left, 1)
    sleep(15)
    ##click on terminal
    mouse.position = (326, 546)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##type command
    keyboard.type('docker run -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    ##sleep
    sleep(45)
    ##change port
    mouse.position = (1152, 374)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1031, 444)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (604, 474)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.type("6080")
    sleep(1)
    mouse.position = (441, 570)
    mouse.click(Button.left, 1)
    sleep(15)
    ##open terminal in new vnc
    mouse.position = (16, 608)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (98, 455)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (251, 480)
    mouse.click(Button.left, 1)
    sleep(1.5)
    ##select on terminal
    mouse.position = (513, 483)
    mouse.click(Button.left, 1)
    sleep(1)
    ##write command
    keyboard.type("sudo apt-get update && sudo apt-get install python3-pip && pip3 install selenium && pip3 install tbselenium && pip3 install pynput && cd /root/Desktop && wget https://www.torproject.org/dist/torbrowser/10.0.15/tor-browser-linux64-10.0.15_en-US.tar.xz && tar -xf tor-browser-linux64-10.0.15_en-US.tar.xz && wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz && tar -xvzf geckodriver-v0.29.1-linux64.tar.gz && rm geckodriver-v0.29.1-linux64.tar.gz && chmod +x geckodriver && sudo cp geckodriver /usr/local/bin/ && cd tor-browser_en-US/Browser/ && rm -r start-tor-browser && wget https://raw.githubusercontent.com/loperkoper/start_tor/main/start-tor-browser && cd /root/Desktop/tor-browser_en-US/Browser/TorBrowser/Data/Tor/ && rm -r torrc && wget https://raw.githubusercontent.com/loperkoper/start_tor/main/torrc && cd /root/Desktop && mkdir tor1 && mkdir tor2 && mkdir tor3 && mkdir tor4 && cp -r /root/Desktop/tor-browser_en-US /root/Desktop/tor1 &&cp -r /root/Desktop/tor-browser_en-US /root/Desktop/tor2 && cp -r /root/Desktop/tor-browser_en-US /root/Desktop/tor3 && cd /root/Desktop && wget https://raw.githubusercontent.com/loperkoper/start_tor/main/script.py && python script.py")
    sleep(1.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(15)
    mouse.position = (513, 483)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.5)
    ##back to first page
    mouse.position = (5, 32)
    mouse.click(Button.left, 1)
    sleep(4)
    ##select stop
    mouse.position = (87, 212)
    mouse.click(Button.left, 1)
    sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(6)
    ##cancel
    mouse.position = (810, 430)
    mouse.click(Button.left, 1)
    sleep(4)
    ##go to setting
    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.type("https://mail.google.com/mail/?logout&hl=en")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)
    ##remove pre account
    sleep(1.5)
    mouse.position = (694, 402)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (848, 326)
    mouse.click(Button.left, 1)
    sleep(2)
    mouse.position = (769, 442)
    mouse.click(Button.left, 1)
    sleep(0.5)
    ##close tab
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    ##back to first page
    mouse.position = (5, 32)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release(Key.ctrl)
    sleep(6)

    ##make vpn on
    on_off_ip()
    
def panj():
    ##clear cookies
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    pyautogui.press('del')
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("shift")
    sleep(2)
    ##click on delet
    mouse.position = (848, 462)
    mouse.click(Button.left, 1)
    sleep(2)

signup()
signin()
panj()
