import math
from datetime import datetime

from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt, QTimer
from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *

from circulariconbutton import CircularIconButton
from downloadthread import DownloadThread
from elidedlabel import ElidedLabel
from imagedownloaderthread import ImageDownloader
from releasetoseekslider import SeekSlider
from resizableiconbutton import ResizableIconButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 640)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.centralwidgetlayout = QHBoxLayout(self.centralwidget)
        self.centralwidgetlayout.setSpacing(0)
        self.centralwidgetlayout.setObjectName(u"centralwidgetlayout")
        self.centralwidgetlayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout_leftMenuContainer = QVBoxLayout(
            self.leftMenuContainer)
        self.verticalLayout_leftMenuContainer.setSpacing(0)
        self.verticalLayout_leftMenuContainer.setObjectName(
            u"verticalLayout_leftMenuContainer")
        self.verticalLayout_leftMenuContainer.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_leftMenuSubContainer = QVBoxLayout(
            self.leftMenuSubContainer)
        self.verticalLayout_leftMenuSubContainer.setSpacing(0)
        self.verticalLayout_leftMenuSubContainer.setObjectName(
            u"verticalLayout_leftMenuSubContainer")
        self.verticalLayout_leftMenuSubContainer.setContentsMargins(0, 0, 0, 0)
        self.menuFrame = QFrame(self.leftMenuSubContainer)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_menuFrame = QHBoxLayout(self.menuFrame)
        self.horizontalLayout_menuFrame.setSpacing(0)
        self.horizontalLayout_menuFrame.setObjectName(
            u"horizontalLayout_menuFrame")
        self.horizontalLayout_menuFrame.setContentsMargins(0, 0, 0, 0)
        self.menuToggleBtn = QPushButton(self.menuFrame)
        self.menuToggleBtn.setObjectName(u"menuToggleBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.menuToggleBtn.setIcon(icon)
        self.menuToggleBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_menuFrame.addWidget(self.menuToggleBtn)

        self.verticalLayout_leftMenuSubContainer.addWidget(
            self.menuFrame, 0, Qt.AlignTop)

        self.mainStackBtnsFrame = QFrame(self.leftMenuSubContainer)
        self.mainStackBtnsFrame.setObjectName(u"mainStackBtnsFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainStackBtnsFrame.sizePolicy().hasHeightForWidth())
        self.mainStackBtnsFrame.setSizePolicy(sizePolicy)
        self.mainStackBtnsFrame.setFrameShape(QFrame.StyledPanel)
        self.mainStackBtnsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_mainStackBtnsFrame = QVBoxLayout(
            self.mainStackBtnsFrame)
        self.verticalLayout_mainStackBtnsFrame.setSpacing(5)
        self.verticalLayout_mainStackBtnsFrame.setObjectName(
            u"verticalLayout_mainStackBtnsFrame")
        self.verticalLayout_mainStackBtnsFrame.setContentsMargins(0, 0, 0, 0)
        self.homeMenuBtn = QPushButton(self.mainStackBtnsFrame)
        self.homeMenuBtn.setObjectName(u"homeMenuBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-home.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.homeMenuBtn.setIcon(icon1)
        self.homeMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_mainStackBtnsFrame.addWidget(self.homeMenuBtn)

        self.downloadMenuBtn = QPushButton(self.mainStackBtnsFrame)
        self.downloadMenuBtn.setObjectName(u"downloadMenuBtn")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.downloadMenuBtn.setFont(font)
        self.downloadMenuBtn.setCursor(QCursor(Qt.ArrowCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-vertical-align-bottom.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.downloadMenuBtn.setIcon(icon2)
        self.downloadMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_mainStackBtnsFrame.addWidget(self.downloadMenuBtn)

        self.fileMenuBtn = QPushButton(self.mainStackBtnsFrame)
        self.fileMenuBtn.setObjectName(u"fileMenuBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-file.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.fileMenuBtn.setIcon(icon3)
        self.fileMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_mainStackBtnsFrame.addWidget(self.fileMenuBtn)

        self.historyMenuBtn = QPushButton(self.mainStackBtnsFrame)
        self.historyMenuBtn.setObjectName(u"historyMenuBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cil-history.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.historyMenuBtn.setIcon(icon4)
        self.historyMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_mainStackBtnsFrame.addWidget(self.historyMenuBtn)

        self.verticalLayout_leftMenuSubContainer.addWidget(
            self.mainStackBtnsFrame, 0, Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_leftMenuSubContainer.addItem(self.verticalSpacer)

        self.settingHelpBtnFrame = QFrame(self.leftMenuSubContainer)
        self.settingHelpBtnFrame.setObjectName(u"settingHelpBtnFrame")
        sizePolicy.setHeightForWidth(
            self.settingHelpBtnFrame.sizePolicy().hasHeightForWidth())
        self.settingHelpBtnFrame.setSizePolicy(sizePolicy)
        self.settingHelpBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.settingHelpBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_settingHelpBtnFrame = QVBoxLayout(
            self.settingHelpBtnFrame)
        self.verticalLayout_settingHelpBtnFrame.setSpacing(0)
        self.verticalLayout_settingHelpBtnFrame.setObjectName(
            u"verticalLayout_settingHelpBtnFrame")
        self.verticalLayout_settingHelpBtnFrame.setContentsMargins(0, 0, 0, 0)
        self.settingsBtn = QPushButton(self.settingHelpBtnFrame)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cil-settings.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_settingHelpBtnFrame.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.settingHelpBtnFrame)
        self.helpBtn.setObjectName(u"helpBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-comment-bubble.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_settingHelpBtnFrame.addWidget(self.helpBtn)

        self.verticalLayout_leftMenuSubContainer.addWidget(
            self.settingHelpBtnFrame, 0, Qt.AlignBottom)

        self.verticalLayout_leftMenuContainer.addWidget(
            self.leftMenuSubContainer)

        self.centralwidgetlayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_centerMenuContainer = QVBoxLayout(
            self.centerMenuContainer)
        self.verticalLayout_centerMenuContainer.setSpacing(0)
        self.verticalLayout_centerMenuContainer.setObjectName(
            u"verticalLayout_centerMenuContainer")
        self.verticalLayout_centerMenuContainer.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.centerMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuSubContainer.setSizePolicy(sizePolicy1)
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.centerMenuSubContainer.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_centerMenuSubContainer = QVBoxLayout(
            self.centerMenuSubContainer)
        self.verticalLayout_centerMenuSubContainer.setSpacing(0)
        self.verticalLayout_centerMenuSubContainer.setObjectName(
            u"verticalLayout_centerMenuSubContainer")
        self.verticalLayout_centerMenuSubContainer.setContentsMargins(
            0, 0, 0, 8)
        self.settingHelpMenu = QStackedWidget(self.centerMenuSubContainer)
        self.settingHelpMenu.setObjectName(u"settingHelpMenu")
        self.settingHelpMenu.setMinimumSize(QSize(200, 0))
        self.settingHelpMenu.setMaximumSize(QSize(16777215, 16777215))
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.settingPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_settingPage = QVBoxLayout(self.settingPage)
        self.verticalLayout_settingPage.setSpacing(0)
        self.verticalLayout_settingPage.setObjectName(
            u"verticalLayout_settingPage")
        self.verticalLayout_settingPage.setContentsMargins(0, 0, 0, 0)
        self.settingMenu = QFrame(self.settingPage)
        self.settingMenu.setObjectName(u"settingMenu")
        self.settingMenu.setFrameShape(QFrame.StyledPanel)
        self.settingMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_settingMenu = QHBoxLayout(self.settingMenu)
        self.horizontalLayout_settingMenu.setSpacing(4)
        self.horizontalLayout_settingMenu.setObjectName(
            u"horizontalLayout_settingMenu")
        self.horizontalLayout_settingMenu.setContentsMargins(4, 4, 4, 4)
        self.settingMenuLabel = QLabel(self.settingMenu)
        self.settingMenuLabel.setObjectName(u"settingMenuLabel")

        self.horizontalLayout_settingMenu.addWidget(
            self.settingMenuLabel, 0, Qt.AlignHCenter)

        self.closeSettingMenuBtn = QPushButton(self.settingMenu)
        self.closeSettingMenuBtn.setObjectName(u"closeSettingMenuBtn")
        self.closeSettingMenuBtn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-x.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.closeSettingMenuBtn.setIcon(icon7)
        self.closeSettingMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_settingMenu.addWidget(
            self.closeSettingMenuBtn, 0, Qt.AlignRight)

        self.verticalLayout_settingPage.addWidget(
            self.settingMenu, 0, Qt.AlignTop)

        self.settingScrollArea = QScrollArea(self.settingPage)
        self.settingScrollArea.setObjectName(u"settingScrollArea")
        self.settingScrollArea.setWidgetResizable(True)
        self.settingScrollAreaContent = QWidget()
        self.settingScrollAreaContent.setObjectName(
            u"settingScrollAreaContent")
        self.settingScrollAreaContent.setGeometry(QRect(0, 0, 196, 675))
        self.verticalLayout_settingScrollAreaContent = QVBoxLayout(
            self.settingScrollAreaContent)
        self.verticalLayout_settingScrollAreaContent.setSpacing(0)
        self.verticalLayout_settingScrollAreaContent.setObjectName(
            u"verticalLayout_settingScrollAreaContent")
        self.verticalLayout_settingScrollAreaContent.setContentsMargins(
            8, 4, 8, 0)
        self.settingScrollAreaWidget = QWidget(self.settingScrollAreaContent)
        self.settingScrollAreaWidget.setObjectName(u"settingScrollAreaWidget")
        self.verticalLayout_settingScrollAreaWidget = QVBoxLayout(
            self.settingScrollAreaWidget)
        self.verticalLayout_settingScrollAreaWidget.setSpacing(0)
        self.verticalLayout_settingScrollAreaWidget.setObjectName(
            u"verticalLayout_settingScrollAreaWidget")
        self.verticalLayout_settingScrollAreaWidget.setContentsMargins(
            0, 0, 0, 0)
        self.settingPageBtnsWidget = QWidget(self.settingScrollAreaWidget)
        self.settingPageBtnsWidget.setObjectName(u"settingPageBtnsWidget")
        self.settingPageBtnsWidget.setStyleSheet(u"")
        self.verticalLayout_settingPageBtnsWidget = QVBoxLayout(
            self.settingPageBtnsWidget)
        self.verticalLayout_settingPageBtnsWidget.setSpacing(0)
        self.verticalLayout_settingPageBtnsWidget.setObjectName(
            u"verticalLayout_settingPageBtnsWidget")
        self.verticalLayout_settingPageBtnsWidget.setContentsMargins(
            0, 0, 0, 0)
        self.settingDefaultFolderLabel = QLabel(self.settingPageBtnsWidget)
        self.settingDefaultFolderLabel.setObjectName(
            u"settingDefaultFolderLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.settingDefaultFolderLabel)

        self.folderSelectBtn = QPushButton(self.settingPageBtnsWidget)
        self.folderSelectBtn.setObjectName(u"folderSelectBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.folderSelectBtn.sizePolicy().hasHeightForWidth())
        self.folderSelectBtn.setSizePolicy(sizePolicy2)
        self.folderSelectBtn.setMinimumSize(QSize(0, 33))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/folder.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.folderSelectBtn.setIcon(icon8)
        self.folderSelectBtn.setIconSize(QSize(14, 14))

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.folderSelectBtn)

        self.settingVideoExtensionLabel = QLabel(self.settingPageBtnsWidget)
        self.settingVideoExtensionLabel.setObjectName(
            u"settingVideoExtensionLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.settingVideoExtensionLabel)

        self.videoExtensionComboBox = QComboBox(self.settingPageBtnsWidget)
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.addItem("")
        self.videoExtensionComboBox.setObjectName(u"videoExtensionComboBox")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.videoExtensionComboBox)

        self.settingAudioExtensionLabel = QLabel(self.settingPageBtnsWidget)
        self.settingAudioExtensionLabel.setObjectName(
            u"settingAudioExtensionLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.settingAudioExtensionLabel)

        self.audioExtensionComboBox = QComboBox(self.settingPageBtnsWidget)
        self.audioExtensionComboBox.addItem("")
        self.audioExtensionComboBox.addItem("")
        self.audioExtensionComboBox.addItem("")
        self.audioExtensionComboBox.addItem("")
        self.audioExtensionComboBox.addItem("")
        self.audioExtensionComboBox.addItem("")
        self.audioExtensionComboBox.setObjectName(u"audioExtensionComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.audioExtensionComboBox.sizePolicy().hasHeightForWidth())
        self.audioExtensionComboBox.setSizePolicy(sizePolicy3)

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.audioExtensionComboBox)

        self.settingPlaySoundLabel = QLabel(self.settingPageBtnsWidget)
        self.settingPlaySoundLabel.setObjectName(u"settingPlaySoundLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.settingPlaySoundLabel)

        self.playSoundBtn = QPushButton(self.settingPageBtnsWidget)
        self.playSoundBtn.setObjectName(u"playSoundBtn")
        self.playSoundBtn.setMinimumSize(QSize(0, 33))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/volume-2.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.playSoundBtn.setIcon(icon9)
        self.playSoundBtn.setIconSize(QSize(14, 14))

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.playSoundBtn)

        self.settingVolumeLabel = QLabel(self.settingPageBtnsWidget)
        self.settingVolumeLabel.setObjectName(u"settingVolumeLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.settingVolumeLabel)

        self.defaultVolumeComboBox = QComboBox(self.settingPageBtnsWidget)
        self.defaultVolumeComboBox.addItem("")
        self.defaultVolumeComboBox.addItem("")
        self.defaultVolumeComboBox.addItem("")
        self.defaultVolumeComboBox.addItem("")
        self.defaultVolumeComboBox.addItem("")
        self.defaultVolumeComboBox.setObjectName(u"defaultVolumeComboBox")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.defaultVolumeComboBox)

        self.settingThemeLabel = QLabel(self.settingPageBtnsWidget)
        self.settingThemeLabel.setObjectName(u"settingThemeLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.settingThemeLabel)

        self.darkModeBtn = QPushButton(self.settingPageBtnsWidget)
        self.darkModeBtn.setObjectName(u"darkModeBtn")
        self.darkModeBtn.setMinimumSize(QSize(0, 33))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/moon.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.darkModeBtn.setIcon(icon10)
        self.darkModeBtn.setIconSize(QSize(14, 14))

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.darkModeBtn)

        self.notificationSoundLabel = QLabel(self.settingPageBtnsWidget)
        self.notificationSoundLabel.setObjectName(u"notificationSoundLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.notificationSoundLabel)

        self.appSoundBtn = QPushButton(self.settingPageBtnsWidget)
        self.appSoundBtn.setObjectName(u"appSoundBtn")

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.appSoundBtn)

        self.forceRescanLabel = QLabel(self.settingPageBtnsWidget)
        self.forceRescanLabel.setObjectName(u"forceRescanLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.forceRescanLabel)

        self.forceRescanBtn = QPushButton(self.settingPageBtnsWidget)
        self.forceRescanBtn.setObjectName(u"forceRescanBtn")

        self.verticalLayout_settingPageBtnsWidget.addWidget(
            self.forceRescanBtn)

        self.randInitLabel = QLabel(self.settingPageBtnsWidget)
        self.randInitLabel.setObjectName(u"randInitLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.randInitLabel)

        self.randInitBtn = QPushButton(self.settingPageBtnsWidget)
        self.randInitBtn.setObjectName(u"randInitBtn")

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.randInitBtn)

        self.loggerLabel = QLabel(self.settingPageBtnsWidget)
        self.loggerLabel.setObjectName(u"loggerLabel")

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.loggerLabel)

        self.loggerBtn = QPushButton(self.settingPageBtnsWidget)
        self.loggerBtn.setObjectName(u"loggerBtn")

        self.verticalLayout_settingPageBtnsWidget.addWidget(self.loggerBtn)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_settingPageBtnsWidget.addItem(
            self.verticalSpacer_7)

        self.verticalLayout_settingScrollAreaWidget.addWidget(
            self.settingPageBtnsWidget)

        self.verticalLayout_settingScrollAreaContent.addWidget(
            self.settingScrollAreaWidget)

        self.settingScrollArea.setWidget(self.settingScrollAreaContent)

        self.verticalLayout_settingPage.addWidget(self.settingScrollArea)

        self.settingHelpMenu.addWidget(self.settingPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_helpPage = QVBoxLayout(self.helpPage)
        self.verticalLayout_helpPage.setSpacing(0)
        self.verticalLayout_helpPage.setObjectName(u"verticalLayout_helpPage")
        self.verticalLayout_helpPage.setContentsMargins(0, 0, 0, 0)
        self.helpMenu = QFrame(self.helpPage)
        self.helpMenu.setObjectName(u"helpMenu")
        self.helpMenu.setFrameShape(QFrame.StyledPanel)
        self.helpMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_helpMenu = QHBoxLayout(self.helpMenu)
        self.horizontalLayout_helpMenu.setSpacing(4)
        self.horizontalLayout_helpMenu.setObjectName(
            u"horizontalLayout_helpMenu")
        self.horizontalLayout_helpMenu.setContentsMargins(4, 4, 4, 4)
        self.helpMenuLabel = QLabel(self.helpMenu)
        self.helpMenuLabel.setObjectName(u"helpMenuLabel")

        self.horizontalLayout_helpMenu.addWidget(
            self.helpMenuLabel, 0, Qt.AlignHCenter)

        self.closeHelpMenuBtn = QPushButton(self.helpMenu)
        self.closeHelpMenuBtn.setObjectName(u"closeHelpMenuBtn")
        self.closeHelpMenuBtn.setIcon(icon7)
        self.closeHelpMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_helpMenu.addWidget(
            self.closeHelpMenuBtn, 0, Qt.AlignRight)

        self.verticalLayout_helpPage.addWidget(self.helpMenu, 0, Qt.AlignTop)

        self.helpTextLabel = QLabel(self.helpPage)
        self.helpTextLabel.setObjectName(u"helpTextLabel")
        self.helpTextLabel.setStyleSheet(u"")
        self.helpTextLabel.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)
        self.helpTextLabel.setWordWrap(True)

        self.verticalLayout_helpPage.addWidget(self.helpTextLabel)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_helpPage.addItem(self.verticalSpacer_8)

        self.settingHelpMenu.addWidget(self.helpPage)

        self.verticalLayout_centerMenuSubContainer.addWidget(
            self.settingHelpMenu)

        self.verticalLayout_centerMenuContainer.addWidget(
            self.centerMenuSubContainer, 0, Qt.AlignLeft)

        self.centralwidgetlayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1.setHeightForWidth(
            self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_mainBodyContainer = QVBoxLayout(
            self.mainBodyContainer)
        self.verticalLayout_mainBodyContainer.setSpacing(0)
        self.verticalLayout_mainBodyContainer.setObjectName(
            u"verticalLayout_mainBodyContainer")
        self.verticalLayout_mainBodyContainer.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_headerContainer = QHBoxLayout(
            self.headerContainer)
        self.horizontalLayout_headerContainer.setSpacing(0)
        self.horizontalLayout_headerContainer.setObjectName(
            u"horizontalLayout_headerContainer")
        self.horizontalLayout_headerContainer.setContentsMargins(0, 0, 0, 0)
        self.appNameFrame = QFrame(self.headerContainer)
        self.appNameFrame.setObjectName(u"appNameFrame")
        self.appNameFrame.setFrameShape(QFrame.StyledPanel)
        self.appNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_appNameFrame = QHBoxLayout(self.appNameFrame)
        self.horizontalLayout_appNameFrame.setSpacing(4)
        self.horizontalLayout_appNameFrame.setObjectName(
            u"horizontalLayout_appNameFrame")
        self.horizontalLayout_appNameFrame.setContentsMargins(4, 0, 0, 0)
        self.youtubeIconBtn = QPushButton(self.appNameFrame)
        self.youtubeIconBtn.setObjectName(u"youtubeIconBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/youtube.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.youtubeIconBtn.setIcon(icon11)

        self.horizontalLayout_appNameFrame.addWidget(
            self.youtubeIconBtn, 0, Qt.AlignVCenter)

        self.appNameLabel = QLabel(self.appNameFrame)
        self.appNameLabel.setObjectName(u"appNameLabel")

        self.horizontalLayout_appNameFrame.addWidget(self.appNameLabel)

        self.horizontalLayout_headerContainer.addWidget(
            self.appNameFrame, 0, Qt.AlignLeft)

        self.headerFrame2 = QFrame(self.headerContainer)
        self.headerFrame2.setObjectName(u"headerFrame2")
        sizePolicy1.setHeightForWidth(
            self.headerFrame2.sizePolicy().hasHeightForWidth())
        self.headerFrame2.setSizePolicy(sizePolicy1)
        self.headerFrame2.setFrameShape(QFrame.StyledPanel)
        self.headerFrame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_headerFrame2 = QHBoxLayout(self.headerFrame2)
        self.horizontalLayout_headerFrame2.setSpacing(0)
        self.horizontalLayout_headerFrame2.setObjectName(
            u"horizontalLayout_headerFrame2")
        self.horizontalLayout_headerFrame2.setContentsMargins(40, 0, 40, 0)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_headerFrame2.addItem(self.horizontalSpacer)

        self.themeBtn = QPushButton(self.headerFrame2)
        self.themeBtn.setObjectName(u"themeBtn")
        self.themeBtn.setMinimumSize(QSize(32, 32))
        self.themeBtn.setMaximumSize(QSize(32, 32))
        self.themeBtn.setSizeIncrement(QSize(0, 0))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/cil-lightbulb.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.themeBtn.setIcon(icon12)
        self.themeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_headerFrame2.addWidget(
            self.themeBtn, 0, Qt.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_headerFrame2.addItem(self.horizontalSpacer_10)

        self.notificationBtn = QPushButton(self.headerFrame2)
        self.notificationBtn.setObjectName(u"notificationBtn")
        self.notificationBtn.setMinimumSize(QSize(32, 32))
        self.notificationBtn.setMaximumSize(QSize(32, 32))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/cil-bell.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon13)
        self.notificationBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_headerFrame2.addWidget(
            self.notificationBtn, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_headerFrame2.addItem(self.horizontalSpacer_2)

        self.speedIconLabel = QLabel(self.headerFrame2)
        self.speedIconLabel.setObjectName(u"speedIconLabel")
        self.speedIconLabel.setMinimumSize(QSize(18, 28))
        self.speedIconLabel.setPixmap(
            QPixmap(u":/icons/icons/cil-speedometer.png"))

        self.horizontalLayout_headerFrame2.addWidget(
            self.speedIconLabel, 0, Qt.AlignHCenter)

        self.internetSpeedLabel = QLabel(self.headerFrame2)
        self.internetSpeedLabel.setObjectName(u"internetSpeedLabel")
        self.internetSpeedLabel.setMinimumSize(QSize(64, 0))
        self.internetSpeedLabel.setMaximumSize(QSize(64, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.internetSpeedLabel.setFont(font1)
        self.internetSpeedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_headerFrame2.addWidget(
            self.internetSpeedLabel, 0, Qt.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_headerFrame2.addItem(self.horizontalSpacer_4)

        self.networkBtn = QPushButton(self.headerFrame2)
        self.networkBtn.setObjectName(u"networkBtn")
        self.networkBtn.setMinimumSize(QSize(32, 32))
        self.networkBtn.setMaximumSize(QSize(32, 32))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/cil-wifi-signal-off.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.networkBtn.setIcon(icon14)
        self.networkBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_headerFrame2.addWidget(
            self.networkBtn, 0, Qt.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_headerFrame2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_headerFrame2.setStretch(0, 5)
        self.horizontalLayout_headerFrame2.setStretch(4, 2)
        self.horizontalLayout_headerFrame2.setStretch(7, 2)
        self.horizontalLayout_headerFrame2.setStretch(9, 5)

        self.horizontalLayout_headerContainer.addWidget(
            self.headerFrame2, 0, Qt.AlignHCenter)

        self.appControlBtnFrame = QFrame(self.headerContainer)
        self.appControlBtnFrame.setObjectName(u"appControlBtnFrame")
        self.appControlBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.appControlBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_appControlBtnFrame = QHBoxLayout(
            self.appControlBtnFrame)
        self.horizontalLayout_appControlBtnFrame.setSpacing(0)
        self.horizontalLayout_appControlBtnFrame.setObjectName(
            u"horizontalLayout_appControlBtnFrame")
        self.horizontalLayout_appControlBtnFrame.setContentsMargins(0, 0, 0, 0)
        self.appMinBtn = QPushButton(self.appControlBtnFrame)
        self.appMinBtn.setObjectName(u"appMinBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/icon_minimize.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.appMinBtn.setIcon(icon15)
        self.appMinBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_appControlBtnFrame.addWidget(self.appMinBtn)

        self.appMaxBtn = QPushButton(self.appControlBtnFrame)
        self.appMaxBtn.setObjectName(u"appMaxBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/icon_maximize.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.appMaxBtn.setIcon(icon16)
        self.appMaxBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_appControlBtnFrame.addWidget(self.appMaxBtn)

        self.appCloseBtn = QPushButton(self.appControlBtnFrame)
        self.appCloseBtn.setObjectName(u"appCloseBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/icon_close.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.appCloseBtn.setIcon(icon17)
        self.appCloseBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_appControlBtnFrame.addWidget(self.appCloseBtn)

        self.horizontalLayout_headerContainer.addWidget(
            self.appControlBtnFrame, 0, Qt.AlignRight)

        self.verticalLayout_mainBodyContainer.addWidget(
            self.headerContainer, 0, Qt.AlignTop)

        self.mainAppBody = QWidget(self.mainBodyContainer)
        self.mainAppBody.setObjectName(u"mainAppBody")
        self.mainAppBody.setStyleSheet(u"")
        self.verticalLayout_mainAppBody = QVBoxLayout(self.mainAppBody)
        self.verticalLayout_mainAppBody.setSpacing(0)
        self.verticalLayout_mainAppBody.setObjectName(
            u"verticalLayout_mainAppBody")
        self.verticalLayout_mainAppBody.setContentsMargins(0, 0, 10, 0)
        self.mainAppStack = QStackedWidget(self.mainAppBody)
        self.mainAppStack.setObjectName(u"mainAppStack")
        self.searchStack = QWidget()
        self.searchStack.setObjectName(u"searchStack")
        self.verticalLayout_searchStack = QVBoxLayout(self.searchStack)
        self.verticalLayout_searchStack.setSpacing(0)
        self.verticalLayout_searchStack.setObjectName(
            u"verticalLayout_searchStack")
        self.verticalLayout_searchStack.setContentsMargins(4, 0, 0, 2)
        self.searchArea = QFrame(self.searchStack)
        self.searchArea.setObjectName(u"searchArea")
        self.searchArea.setFrameShape(QFrame.StyledPanel)
        self.searchArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_searchArea = QHBoxLayout(self.searchArea)
        self.horizontalLayout_searchArea.setSpacing(0)
        self.horizontalLayout_searchArea.setObjectName(
            u"horizontalLayout_searchArea")
        self.horizontalLayout_searchArea.setContentsMargins(0, 24, 0, 16)
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_searchArea.addItem(self.horizontalSpacer_5)

        self.searchInputText = QLineEdit(self.searchArea)
        self.searchInputText.setObjectName(u"searchInputText")
        self.searchInputText.setMinimumSize(QSize(0, 0))
        self.searchInputText.setMaximumSize(QSize(720, 16777215))
        self.searchInputText.setStyleSheet(u"")
        self.searchInputText.setAcceptDrops(True)

        self.horizontalLayout_searchArea.addWidget(self.searchInputText)

        self.searchBtn = QPushButton(self.searchArea)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setStyleSheet(u"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/cil-magnifying-glass.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon18)
        self.searchBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_searchArea.addWidget(self.searchBtn)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_searchArea.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_searchArea.setStretch(1, 2)

        self.verticalLayout_searchStack.addWidget(
            self.searchArea, 0, Qt.AlignTop)

        self.searchResultFrame = QFrame(self.searchStack)
        self.searchResultFrame.setObjectName(u"searchResultFrame")
        self.searchResultFrame.setFrameShape(QFrame.StyledPanel)
        self.searchResultFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_searchResultFrame = QHBoxLayout(
            self.searchResultFrame)
        self.horizontalLayout_searchResultFrame.setSpacing(0)
        self.horizontalLayout_searchResultFrame.setObjectName(
            u"horizontalLayout_searchResultFrame")
        self.horizontalLayout_searchResultFrame.setContentsMargins(0, 0, 6, 4)
        self.scrollArea = QScrollArea(self.searchResultFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 641, 404))
        self.horizontalLayout_scrollAreaWidgetContents = QHBoxLayout(
            self.scrollAreaWidgetContents)
        self.horizontalLayout_scrollAreaWidgetContents.setSpacing(0)
        self.horizontalLayout_scrollAreaWidgetContents.setObjectName(
            u"horizontalLayout_scrollAreaWidgetContents")
        self.horizontalLayout_scrollAreaWidgetContents.setContentsMargins(
            0, 0, 0, 0)
        self.videoSpaceFrame = QFrame(self.scrollAreaWidgetContents)
        self.videoSpaceFrame.setObjectName(u"videoSpaceFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.videoSpaceFrame.sizePolicy().hasHeightForWidth())
        self.videoSpaceFrame.setSizePolicy(sizePolicy4)
        self.videoSpaceFrame.setFrameShape(QFrame.StyledPanel)
        self.videoSpaceFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_videoSpaceFrame = QGridLayout(self.videoSpaceFrame)
        self.gridLayout_videoSpaceFrame.setSpacing(4)
        self.gridLayout_videoSpaceFrame.setObjectName(
            u"gridLayout_videoSpaceFrame")
        self.gridLayout_videoSpaceFrame.setContentsMargins(0, 8, 0, 4)
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_videoSpaceFrame.addItem(
            self.verticalSpacer_2, 0, 0, 1, 1)
        # video container was here

        self.horizontalLayout_scrollAreaWidgetContents.addWidget(
            self.videoSpaceFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_searchResultFrame.addWidget(self.scrollArea)

        self.verticalLayout_searchStack.addWidget(self.searchResultFrame)

        self.mainAppStack.addWidget(self.searchStack)
        self.loadingStack = QWidget()
        self.loadingStack.setObjectName(u"loadingStack")
        self.verticalLayout_loadingStack = QVBoxLayout(self.loadingStack)
        self.verticalLayout_loadingStack.setObjectName(
            u"verticalLayout_loadingStack")
        self.loadingWidget = QWidget(self.loadingStack)
        self.loadingWidget.setObjectName(u"loadingWidget")
        self.verticalLayout_loadingWidget = QVBoxLayout(self.loadingWidget)
        self.verticalLayout_loadingWidget.setObjectName(
            u"verticalLayout_loadingWidget")
        self.loadingIcon = QLabel(self.loadingWidget)
        self.loadingIcon.setObjectName(u"loadingIcon")
        self.loadingIcon.setMinimumSize(QSize(128, 102))
        self.loadingIcon.setMaximumSize(QSize(128, 102))
        self.loadingIcon.setScaledContents(True)

        self.verticalLayout_loadingWidget.addWidget(
            self.loadingIcon, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.loadingFrame = QFrame(self.loadingWidget)
        self.loadingFrame.setObjectName(u"loadingFrame")
        self.loadingFrame.setMaximumSize(QSize(144, 16777215))
        self.loadingFrame.setFrameShape(QFrame.StyledPanel)
        self.loadingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_loadingFrame = QVBoxLayout(self.loadingFrame)
        self.verticalLayout_loadingFrame.setSpacing(4)
        self.verticalLayout_loadingFrame.setObjectName(
            u"verticalLayout_loadingFrame")
        self.verticalLayout_loadingFrame.setContentsMargins(0, 0, 0, 0)
        self.loadingLabel = QLabel(self.loadingFrame)
        self.loadingLabel.setObjectName(u"loadingLabel")

        self.verticalLayout_loadingFrame.addWidget(
            self.loadingLabel, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_loadingWidget.addWidget(self.loadingFrame)

        self.verticalLayout_loadingStack.addWidget(
            self.loadingWidget, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.mainAppStack.addWidget(self.loadingStack)
        self.initStack = QWidget()
        self.initStack.setObjectName(u"initStack")
        self.verticalLayout_initStack = QVBoxLayout(self.initStack)
        self.verticalLayout_initStack.setObjectName(
            u"verticalLayout_initStack")
        self.initWidget = QWidget(self.initStack)
        self.initWidget.setObjectName(u"initWidget")
        self.verticalLayout_initWidget = QVBoxLayout(self.initWidget)
        self.verticalLayout_initWidget.setObjectName(
            u"verticalLayout_initWidget")
        self.initIcon = QLabel(self.initWidget)
        self.initIcon.setObjectName(u"initIcon")
        self.initIcon.setMinimumSize(QSize(128, 102))
        self.initIcon.setMaximumSize(QSize(128, 102))
        self.initIcon.setScaledContents(True)

        self.verticalLayout_initWidget.addWidget(
            self.initIcon, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.initFrame = QFrame(self.initWidget)
        self.initFrame.setObjectName(u"initFrame")
        self.initFrame.setMaximumSize(QSize(144, 16777215))
        self.initFrame.setFrameShape(QFrame.StyledPanel)
        self.initFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_initFrame = QVBoxLayout(self.initFrame)
        self.verticalLayout_initFrame.setSpacing(4)
        self.verticalLayout_initFrame.setObjectName(
            u"verticalLayout_initFrame")
        self.verticalLayout_initFrame.setContentsMargins(0, 0, 0, 0)
        self.initLabel = QLabel(self.initFrame)
        self.initLabel.setObjectName(u"initLabel")

        self.verticalLayout_initFrame.addWidget(self.initLabel)

        self.verticalLayout_initWidget.addWidget(
            self.initFrame, 0, Qt.AlignHCenter)

        self.verticalLayout_initStack.addWidget(
            self.initWidget, 0, Qt.AlignVCenter)

        self.mainAppStack.addWidget(self.initStack)
        self.downloadStack = QWidget()
        self.downloadStack.setObjectName(u"downloadStack")
        self.verticalLayout_downloadStack = QVBoxLayout(self.downloadStack)
        self.verticalLayout_downloadStack.setSpacing(0)
        self.verticalLayout_downloadStack.setObjectName(
            u"verticalLayout_downloadStack")
        self.verticalLayout_downloadStack.setContentsMargins(4, 0, 4, 2)
        self.downloadWidget = QWidget(self.downloadStack)
        self.downloadWidget.setObjectName(u"downloadWidget")
        self.downloadWidget.setStyleSheet(u"")
        self.verticalLayout_downloadWidget = QVBoxLayout(self.downloadWidget)
        self.verticalLayout_downloadWidget.setSpacing(0)
        self.verticalLayout_downloadWidget.setObjectName(
            u"verticalLayout_downloadWidget")
        self.verticalLayout_downloadWidget.setContentsMargins(0, 0, 0, 0)
        self.downloadsMainLabel = QLabel(self.downloadWidget)
        self.downloadsMainLabel.setObjectName(u"downloadsMainLabel")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.downloadsMainLabel.setFont(font2)
        self.downloadsMainLabel.setStyleSheet(u"")

        self.verticalLayout_downloadWidget.addWidget(self.downloadsMainLabel)

        self.downloadsScrollArea = QScrollArea(self.downloadWidget)
        self.downloadsScrollArea.setObjectName(u"downloadsScrollArea")
        self.downloadsScrollArea.setStyleSheet(u"")
        self.downloadsScrollArea.setWidgetResizable(True)
        self.downloadsAreaWidget = QWidget()
        self.downloadsAreaWidget.setObjectName(u"downloadsAreaWidget")
        self.downloadsAreaWidget.setGeometry(QRect(0, 0, 670, 436))
        self.downloadsAreaWidget.setStyleSheet(u"")
        self.verticalLayout_downloadsAreaWidget = QVBoxLayout(
            self.downloadsAreaWidget)
        self.verticalLayout_downloadsAreaWidget.setSpacing(4)
        self.verticalLayout_downloadsAreaWidget.setObjectName(
            u"verticalLayout_downloadsAreaWidget")
        self.verticalLayout_downloadsAreaWidget.setContentsMargins(0, 0, 0, 0)
        # download item frame was here

        # home redirect button was here

        self.downloadsScrollArea.setWidget(self.downloadsAreaWidget)

        self.verticalLayout_downloadWidget.addWidget(self.downloadsScrollArea)

        self.verticalLayout_downloadStack.addWidget(self.downloadWidget)

        self.mainAppStack.addWidget(self.downloadStack)
        self.filesStack = QWidget()
        self.filesStack.setObjectName(u"filesStack")
        self.filesStack.setStyleSheet(u"")
        self.verticalLayout_filesStack = QVBoxLayout(self.filesStack)
        self.verticalLayout_filesStack.setSpacing(0)
        self.verticalLayout_filesStack.setObjectName(
            u"verticalLayout_filesStack")
        self.verticalLayout_filesStack.setContentsMargins(4, 0, 4, 2)
        self.fileStackWidget = QWidget(self.filesStack)
        self.fileStackWidget.setObjectName(u"fileStackWidget")
        self.verticalLayout_fileStackWidget = QVBoxLayout(self.fileStackWidget)
        self.verticalLayout_fileStackWidget.setSpacing(0)
        self.verticalLayout_fileStackWidget.setObjectName(
            u"verticalLayout_fileStackWidget")
        self.verticalLayout_fileStackWidget.setContentsMargins(0, 0, 0, 2)
        self.filesHeaderFrame = QFrame(self.fileStackWidget)
        self.filesHeaderFrame.setObjectName(u"filesHeaderFrame")
        self.filesHeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.filesHeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.filesHeaderFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.filesLabel = QLabel(self.filesHeaderFrame)
        self.filesLabel.setObjectName(u"filesLabel")
        self.filesLabel.setFont(font2)
        self.filesLabel.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.filesLabel)

        self.filesUtilityFrame = QFrame(self.filesHeaderFrame)
        self.filesUtilityFrame.setObjectName(u"filesUtilityFrame")
        self.filesUtilityFrame.setFrameShape(QFrame.StyledPanel)
        self.filesUtilityFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.filesUtilityFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 0, 8, 0)

        self.sortByLabel = QLabel(self.filesUtilityFrame)
        self.sortByLabel.setObjectName(u"sortByLabel")
        self.sortByLabel.setMinimumSize(QSize(56, 0))
        self.sortByLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.sortByLabel)

        self.filesSortComboBox = QComboBox(self.filesUtilityFrame)
        self.filesSortComboBox.addItem("")
        self.filesSortComboBox.addItem("")
        self.filesSortComboBox.addItem("")
        self.filesSortComboBox.addItem("")
        self.filesSortComboBox.setObjectName(u"filesSortComboBox")
        self.filesSortComboBox.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.filesSortComboBox)

        self.horizontalLayout.addWidget(
            self.filesUtilityFrame, 0, Qt.AlignRight)

        self.verticalLayout_fileStackWidget.addWidget(self.filesHeaderFrame)

        self.filesScrollArea = QScrollArea(self.fileStackWidget)
        self.filesScrollArea.setObjectName(u"filesScrollArea")
        self.filesScrollArea.setWidgetResizable(True)
        self.filesScrollAreaContents = QWidget()
        self.filesScrollAreaContents.setObjectName(u"filesScrollAreaContents")
        self.filesScrollAreaContents.setGeometry(QRect(0, 0, 643, 361))
        self.filesScrollAreaContents.setStyleSheet(u"")
        self.verticalLayout_filesScrollAreaContents = QVBoxLayout(
            self.filesScrollAreaContents)
        self.verticalLayout_filesScrollAreaContents.setSpacing(4)
        self.verticalLayout_filesScrollAreaContents.setObjectName(
            u"verticalLayout_filesScrollAreaContents")
        self.verticalLayout_filesScrollAreaContents.setContentsMargins(
            0, 0, 0, 0)
        # Files was here

        # end of file button was here
        self.filesScrollArea.setWidget(self.filesScrollAreaContents)

        self.verticalLayout_fileStackWidget.addWidget(self.filesScrollArea)

        self.mediaPlayer = QWidget(self.fileStackWidget)
        self.mediaPlayer.setObjectName(u"mediaPlayer")
        sizePolicy.setHeightForWidth(
            self.mediaPlayer.sizePolicy().hasHeightForWidth())
        self.mediaPlayer.setSizePolicy(sizePolicy)
        self.mediaPlayer.setMinimumSize(QSize(0, 0))
        self.mediaPlayer.setMaximumSize(QSize(16777215, 16777215))
        self.mediaPlayer.setStyleSheet(u"")
        self.verticalLayout_mediaPlayer = QVBoxLayout(self.mediaPlayer)
        self.verticalLayout_mediaPlayer.setSpacing(0)
        self.verticalLayout_mediaPlayer.setObjectName(
            u"verticalLayout_mediaPlayer")
        self.verticalLayout_mediaPlayer.setContentsMargins(0, 1, 0, 1)
        self.videoPlaybackFrame = QFrame(self.mediaPlayer)
        self.videoPlaybackFrame.setObjectName(u"videoPlaybackFrame")
        self.videoPlaybackFrame.setFrameShape(QFrame.StyledPanel)
        self.videoPlaybackFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_videoPlaybackFrame = QVBoxLayout(
            self.videoPlaybackFrame)
        self.verticalLayout_videoPlaybackFrame.setSpacing(0)
        self.verticalLayout_videoPlaybackFrame.setObjectName(
            u"verticalLayout_videoPlaybackFrame")
        self.verticalLayout_videoPlaybackFrame.setContentsMargins(0, 0, 0, 0)
        self.playerTitleLabel = QLabel(self.videoPlaybackFrame)
        self.playerTitleLabel.setObjectName(u"playerTitleLabel")
        self.playerTitleLabel.setStyleSheet(u"")

        self.verticalLayout_videoPlaybackFrame.addWidget(
            self.playerTitleLabel, 0, Qt.AlignLeft)

        self.videoOutputFrame = QVideoWidget(self.videoPlaybackFrame)
        self.videoOutputFrame.setObjectName(u"videoOutputFrame")

        self.verticalLayout_videoPlaybackFrame.addWidget(self.videoOutputFrame)

        self.verticalLayout_mediaPlayer.addWidget(self.videoPlaybackFrame)

        self.playerControllerFrame = QFrame(self.mediaPlayer)
        self.playerControllerFrame.setObjectName(u"playerControllerFrame")
        self.playerControllerFrame.setFrameShape(QFrame.StyledPanel)
        self.playerControllerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_playerControllerFrame = QHBoxLayout(
            self.playerControllerFrame)
        self.horizontalLayout_playerControllerFrame.setSpacing(0)
        self.horizontalLayout_playerControllerFrame.setObjectName(
            u"horizontalLayout_playerControllerFrame")
        self.horizontalLayout_playerControllerFrame.setContentsMargins(
            0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_playerControllerFrame.addItem(
            self.horizontalSpacer_13)

        self.mediaPlayerFrame = QFrame(self.playerControllerFrame)
        self.mediaPlayerFrame.setObjectName(u"mediaPlayerFrame")
        self.mediaPlayerFrame.setMinimumSize(QSize(560, 40))
        self.mediaPlayerFrame.setMaximumSize(QSize(600, 48))
        self.mediaPlayerFrame.setAcceptDrops(True)
        self.mediaPlayerFrame.setStyleSheet(u"")
        self.mediaPlayerFrame.setFrameShape(QFrame.StyledPanel)
        self.mediaPlayerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_mediaPlayerFrame = QVBoxLayout(
            self.mediaPlayerFrame)
        self.verticalLayout_mediaPlayerFrame.setSpacing(0)
        self.verticalLayout_mediaPlayerFrame.setObjectName(
            u"verticalLayout_mediaPlayerFrame")
        self.verticalLayout_mediaPlayerFrame.setContentsMargins(1, 0, 1, 0)
        self.mediaProgressFrame = QFrame(self.mediaPlayerFrame)
        self.mediaProgressFrame.setObjectName(u"mediaProgressFrame")
        self.mediaProgressFrame.setStyleSheet(u"")
        self.mediaProgressFrame.setFrameShape(QFrame.StyledPanel)
        self.mediaProgressFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_mediaProgressFrame = QHBoxLayout(
            self.mediaProgressFrame)
        self.horizontalLayout_mediaProgressFrame.setSpacing(8)
        self.horizontalLayout_mediaProgressFrame.setObjectName(
            u"horizontalLayout_mediaProgressFrame")
        self.horizontalLayout_mediaProgressFrame.setContentsMargins(8, 0, 8, 0)
        self.currentPlayingTimeLabel = QLabel(self.mediaProgressFrame)
        self.currentPlayingTimeLabel.setObjectName(u"currentPlayingTimeLabel")
        sizePolicy4.setHeightForWidth(
            self.currentPlayingTimeLabel.sizePolicy().hasHeightForWidth())
        self.currentPlayingTimeLabel.setSizePolicy(sizePolicy4)
        self.currentPlayingTimeLabel.setMinimumSize(QSize(44, 16))
        self.currentPlayingTimeLabel.setMaximumSize(QSize(44, 16))
        self.currentPlayingTimeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_mediaProgressFrame.addWidget(
            self.currentPlayingTimeLabel)

        self.playbackProgress = SeekSlider(
            Qt.Horizontal, parent=self.mediaProgressFrame)
        self.playbackProgress.setObjectName(u"playbackProgress")
        self.playbackProgress.setMinimumSize(QSize(440, 8))
        self.playbackProgress.setMaximumSize(QSize(16777215, 8))
        self.playbackProgress.setOrientation(Qt.Horizontal)

        self.horizontalLayout_mediaProgressFrame.addWidget(
            self.playbackProgress)

        self.mediaLengthLabel = QLabel(self.mediaProgressFrame)
        self.mediaLengthLabel.setObjectName(u"mediaLengthLabel")
        self.mediaLengthLabel.setMinimumSize(QSize(44, 16))
        self.mediaLengthLabel.setMaximumSize(QSize(44, 16))
        font3 = QFont()
        font3.setFamily(u"Helvetica")
        self.mediaLengthLabel.setFont(font3)
        self.mediaLengthLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_mediaProgressFrame.addWidget(
            self.mediaLengthLabel)

        self.verticalLayout_mediaPlayerFrame.addWidget(self.mediaProgressFrame)

        self.mediaButtonsFrame = QFrame(self.mediaPlayerFrame)
        self.mediaButtonsFrame.setObjectName(u"mediaButtonsFrame")
        self.mediaButtonsFrame.setStyleSheet(u"")
        self.mediaButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.mediaButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_mediaButtonsFrame = QHBoxLayout(
            self.mediaButtonsFrame)
        self.horizontalLayout_mediaButtonsFrame.setSpacing(2)
        self.horizontalLayout_mediaButtonsFrame.setObjectName(
            u"horizontalLayout_mediaButtonsFrame")
        self.horizontalLayout_mediaButtonsFrame.setContentsMargins(8, 0, 10, 0)
        self.fileOpenBtn = QPushButton(self.mediaButtonsFrame)
        self.fileOpenBtn.setObjectName(u"fileOpenBtn")
        self.fileOpenBtn.setMinimumSize(QSize(22, 22))
        self.fileOpenBtn.setMaximumSize(QSize(22, 22))
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/cil-folder-open.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.fileOpenBtn.setIcon(icon23)
        self.fileOpenBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.fileOpenBtn, 0, Qt.AlignLeft)

        self.mediaLockBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaLockBtn.setObjectName(u"mediaLockBtn")
        self.mediaLockBtn.setMinimumSize(QSize(22, 22))
        self.mediaLockBtn.setMaximumSize(QSize(22, 22))
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/cil-lock-locked.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaLockBtn.setIcon(icon24)
        self.mediaLockBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.mediaLockBtn, 0, Qt.AlignLeft)

        self.mediaTitleLabel = QLabel(self.mediaButtonsFrame)
        self.mediaTitleLabel.setObjectName(u"mediaTitleLabel")
        self.mediaTitleLabel.setMinimumSize(QSize(140, 18))
        self.mediaTitleLabel.setMaximumSize(QSize(170, 22))
        self.mediaTitleLabel.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.mediaTitleLabel)

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_mediaButtonsFrame.addItem(
            self.horizontalSpacer_12)

        self.seekBackwardBtn = QPushButton(self.mediaButtonsFrame)
        self.seekBackwardBtn.setObjectName(u"seekBackwardBtn")
        self.seekBackwardBtn.setMinimumSize(QSize(22, 22))
        self.seekBackwardBtn.setMaximumSize(QSize(22, 22))
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/cil-media-skip-backward.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.seekBackwardBtn.setIcon(icon25)
        self.seekBackwardBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.seekBackwardBtn)

        self.mediaPreviousBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaPreviousBtn.setObjectName(u"mediaPreviousBtn")
        self.mediaPreviousBtn.setMinimumSize(QSize(22, 22))
        self.mediaPreviousBtn.setMaximumSize(QSize(22, 22))
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/cil-media-step-backward.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaPreviousBtn.setIcon(icon26)
        self.mediaPreviousBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.mediaPreviousBtn, 0, Qt.AlignHCenter)

        self.mediaPlayBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaPlayBtn.setObjectName(u"mediaPlayBtn")
        self.mediaPlayBtn.setMinimumSize(QSize(22, 22))
        self.mediaPlayBtn.setMaximumSize(QSize(22, 22))
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/cil-media-play.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaPlayBtn.setIcon(icon27)
        self.mediaPlayBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.mediaPlayBtn, 0, Qt.AlignHCenter)

        self.mediaNextBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaNextBtn.setObjectName(u"mediaNextBtn")
        self.mediaNextBtn.setMinimumSize(QSize(22, 22))
        self.mediaNextBtn.setMaximumSize(QSize(22, 22))
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/cil-media-step-forward.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaNextBtn.setIcon(icon28)
        self.mediaNextBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.mediaNextBtn, 0, Qt.AlignHCenter)

        self.seekForwardBtn = QPushButton(self.mediaButtonsFrame)
        self.seekForwardBtn.setObjectName(u"seekForwardBtn")
        self.seekForwardBtn.setMinimumSize(QSize(22, 22))
        self.seekForwardBtn.setMaximumSize(QSize(22, 22))
        icon29 = QIcon()
        icon29.addFile(u":/icons/icons/cil-media-skip-forward.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.seekForwardBtn.setIcon(icon29)
        self.seekForwardBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.seekForwardBtn)

        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_mediaButtonsFrame.addItem(
            self.horizontalSpacer_11)

        self.mediaRepeatBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaRepeatBtn.setObjectName(u"mediaRepeatBtn")
        self.mediaRepeatBtn.setMinimumSize(QSize(22, 22))
        self.mediaRepeatBtn.setMaximumSize(QSize(22, 22))
        icon30 = QIcon()
        icon30.addFile(u":/icons/icons/cil-loop.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaRepeatBtn.setIcon(icon30)
        self.mediaRepeatBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.mediaRepeatBtn)

        self.mediaShuffleBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaShuffleBtn.setObjectName(u"mediaShuffleBtn")
        self.mediaShuffleBtn.setMinimumSize(QSize(22, 22))
        self.mediaShuffleBtn.setMaximumSize(QSize(22, 22))
        icon31 = QIcon()
        icon31.addFile(u":/icons/icons/cil-infinity.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaShuffleBtn.setIcon(icon31)
        self.mediaShuffleBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.mediaShuffleBtn)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_mediaButtonsFrame.addItem(
            self.horizontalSpacer_9)

        self.playbackSpeedCombobox = QComboBox(self.mediaButtonsFrame)
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.addItem("")
        self.playbackSpeedCombobox.setObjectName(u"playbackSpeedCombobox")
        self.playbackSpeedCombobox.setMinimumSize(QSize(28, 22))
        self.playbackSpeedCombobox.setMaximumSize(QSize(28, 22))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.playbackSpeedCombobox.setFont(font4)

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.playbackSpeedCombobox)

        self.videoWidgetBtn = QPushButton(self.mediaButtonsFrame)
        self.videoWidgetBtn.setObjectName(u"videoWidgetBtn")
        self.videoWidgetBtn.setMinimumSize(QSize(22, 22))
        self.videoWidgetBtn.setMaximumSize(QSize(22, 22))
        icon32 = QIcon()
        icon32.addFile(u":/icons/icons/cil-input.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.videoWidgetBtn.setIcon(icon32)
        self.videoWidgetBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.videoWidgetBtn)

        self.mediaMuteBtn = QPushButton(self.mediaButtonsFrame)
        self.mediaMuteBtn.setObjectName(u"mediaMuteBtn")
        self.mediaMuteBtn.setMinimumSize(QSize(22, 22))
        self.mediaMuteBtn.setMaximumSize(QSize(22, 22))
        icon33 = QIcon()
        icon33.addFile(u":/icons/icons/cil-volume-high.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.mediaMuteBtn.setIcon(icon33)
        self.mediaMuteBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.mediaMuteBtn, 0, Qt.AlignRight)

        self.mediaVolumeSlider = SeekSlider(
            Qt.Horizontal, parent=self.mediaButtonsFrame)
        self.mediaVolumeSlider.setObjectName(u"mediaVolumeSlider")
        self.mediaVolumeSlider.setMinimumSize(QSize(64, 22))
        self.mediaVolumeSlider.setMaximumSize(QSize(16777215, 24))
        self.mediaVolumeSlider.setStyleSheet(u"")
        self.mediaVolumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_mediaButtonsFrame.addWidget(
            self.mediaVolumeSlider, 0, Qt.AlignRight)

        self.playerOffBtn = QPushButton(self.mediaButtonsFrame)
        self.playerOffBtn.setObjectName(u"playerOffBtn")
        self.playerOffBtn.setMinimumSize(QSize(22, 22))
        self.playerOffBtn.setMaximumSize(QSize(22, 22))
        icon34 = QIcon()
        icon34.addFile(u":/icons/icons/cil-media-stop.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.playerOffBtn.setIcon(icon34)

        self.horizontalLayout_mediaButtonsFrame.addWidget(self.playerOffBtn)

        self.verticalLayout_mediaPlayerFrame.addWidget(self.mediaButtonsFrame)

        self.horizontalLayout_playerControllerFrame.addWidget(
            self.mediaPlayerFrame)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_playerControllerFrame.addItem(
            self.horizontalSpacer_14)

        self.horizontalLayout_playerControllerFrame.setStretch(0, 1)
        self.horizontalLayout_playerControllerFrame.setStretch(1, 2)
        self.horizontalLayout_playerControllerFrame.setStretch(2, 1)

        self.verticalLayout_mediaPlayer.addWidget(self.playerControllerFrame)

        self.verticalLayout_fileStackWidget.addWidget(
            self.mediaPlayer, 0, Qt.AlignBottom)

        self.verticalLayout_filesStack.addWidget(self.fileStackWidget)

        self.mainAppStack.addWidget(self.filesStack)
        self.historyStack = QWidget()
        self.historyStack.setObjectName(u"historyStack")
        self.historyStack.setStyleSheet(u"")
        self.verticalLayout_historyStack = QVBoxLayout(self.historyStack)
        self.verticalLayout_historyStack.setSpacing(0)
        self.verticalLayout_historyStack.setObjectName(
            u"verticalLayout_historyStack")
        self.verticalLayout_historyStack.setContentsMargins(4, 0, 4, 2)
        self.historyStackWidget = QWidget(self.historyStack)
        self.historyStackWidget.setObjectName(u"historyStackWidget")
        self.verticalLayout_historyStackWidget = QVBoxLayout(
            self.historyStackWidget)
        self.verticalLayout_historyStackWidget.setSpacing(0)
        self.verticalLayout_historyStackWidget.setObjectName(
            u"verticalLayout_historyStackWidget")
        self.verticalLayout_historyStackWidget.setContentsMargins(0, 0, 0, 0)
        self.historyStackLabel = QLabel(self.historyStackWidget)
        self.historyStackLabel.setObjectName(u"historyStackLabel")
        self.historyStackLabel.setFont(font2)

        self.verticalLayout_historyStackWidget.addWidget(
            self.historyStackLabel)

        self.historyScrollArea = QScrollArea(self.historyStackWidget)
        self.historyScrollArea.setObjectName(u"historyScrollArea")
        self.historyScrollArea.setWidgetResizable(True)
        self.historyScrollContent = QWidget()
        self.historyScrollContent.setObjectName(u"historyScrollContent")
        self.historyScrollContent.setGeometry(QRect(0, 0, 643, 440))
        self.verticalLayout_historyScrollContent = QVBoxLayout(
            self.historyScrollContent)
        self.verticalLayout_historyScrollContent.setSpacing(4)
        self.verticalLayout_historyScrollContent.setObjectName(
            u"verticalLayout_historyScrollContent")
        self.verticalLayout_historyScrollContent.setContentsMargins(0, 0, 0, 0)
        # history item was here

        self.historyLastItemFrame = QFrame(self.historyScrollContent)
        self.historyLastItemFrame.setObjectName(u"historyLastItemFrame")
        self.historyLastItemFrame.setMinimumSize(QSize(0, 85))
        self.historyLastItemFrame.setStyleSheet(u"")
        self.historyLastItemFrame.setFrameShape(QFrame.StyledPanel)
        self.historyLastItemFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_historyLastItemFrame = QVBoxLayout(
            self.historyLastItemFrame)
        self.verticalLayout_historyLastItemFrame.setSpacing(0)
        self.verticalLayout_historyLastItemFrame.setObjectName(
            u"verticalLayout_historyLastItemFrame")
        self.verticalLayout_historyLastItemFrame.setContentsMargins(0, 0, 0, 0)

        self.historyScrollArea.setWidget(self.historyScrollContent)

        self.verticalLayout_historyStackWidget.addWidget(
            self.historyScrollArea)

        self.verticalLayout_historyStack.addWidget(self.historyStackWidget)

        self.mainAppStack.addWidget(self.historyStack)

        self.verticalLayout_mainAppBody.addWidget(self.mainAppStack)

        self.notificationWiget = QWidget(self.mainAppBody)
        self.notificationWiget.setObjectName(u"notificationWiget")
        self.notificationWiget.setMaximumSize(QSize(16777215, 16777215))
        self.notificationWiget.setSizeIncrement(QSize(0, 40))
        self.verticalLayout_notificationWiget = QVBoxLayout(
            self.notificationWiget)
        self.verticalLayout_notificationWiget.setSpacing(0)
        self.verticalLayout_notificationWiget.setObjectName(
            u"verticalLayout_notificationWiget")
        self.verticalLayout_notificationWiget.setContentsMargins(0, 0, 0, 0)
        self.notificationFrame = QFrame(self.notificationWiget)
        self.notificationFrame.setObjectName(u"notificationFrame")
        self.notificationFrame.setMaximumSize(QSize(16777215, 16777215))
        self.notificationFrame.setFrameShape(QFrame.StyledPanel)
        self.notificationFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_notificationFrame = QHBoxLayout(
            self.notificationFrame)
        self.horizontalLayout_notificationFrame.setSpacing(0)
        self.horizontalLayout_notificationFrame.setObjectName(
            u"horizontalLayout_notificationFrame")
        self.horizontalLayout_notificationFrame.setContentsMargins(0, 0, 0, 0)
        self.notificationLabel = QLabel(self.notificationFrame)
        self.notificationLabel.setObjectName(u"notificationLabel")
        sizePolicy1.setHeightForWidth(
            self.notificationLabel.sizePolicy().hasHeightForWidth())
        self.notificationLabel.setSizePolicy(sizePolicy1)
        self.notificationLabel.setWordWrap(True)

        self.horizontalLayout_notificationFrame.addWidget(
            self.notificationLabel)

        self.clearNotificationBtn = QPushButton(self.notificationFrame)
        self.clearNotificationBtn.setObjectName(u"clearNotificationBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.clearNotificationBtn.sizePolicy().hasHeightForWidth())
        self.clearNotificationBtn.setSizePolicy(sizePolicy7)
        self.clearNotificationBtn.setMinimumSize(QSize(0, 0))
        self.clearNotificationBtn.setMaximumSize(QSize(16777215, 24))
        icon35 = QIcon()
        icon35.addFile(u":/icons/icons/x-square.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.clearNotificationBtn.setIcon(icon35)
        self.clearNotificationBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_notificationFrame.addWidget(
            self.clearNotificationBtn, 0, Qt.AlignRight)

        self.verticalLayout_notificationWiget.addWidget(self.notificationFrame)

        self.verticalLayout_mainAppBody.addWidget(self.notificationWiget)

        self.verticalLayout_mainBodyContainer.addWidget(self.mainAppBody)

        self.footer = QWidget(self.mainBodyContainer)
        self.footer.setObjectName(u"footer")
        self.verticalLayout_footer = QVBoxLayout(self.footer)
        self.verticalLayout_footer.setSpacing(0)
        self.verticalLayout_footer.setObjectName(u"verticalLayout_footer")
        self.verticalLayout_footer.setContentsMargins(0, 0, 0, 0)
        self.footerFrame = QFrame(self.footer)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_footerFrame = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_footerFrame.setSpacing(8)
        self.horizontalLayout_footerFrame.setObjectName(
            u"horizontalLayout_footerFrame")
        self.horizontalLayout_footerFrame.setContentsMargins(0, 4, 0, 0)
        self.footerLabel = QLabel(self.footerFrame)
        self.footerLabel.setObjectName(u"footerLabel")

        self.horizontalLayout_footerFrame.addWidget(
            self.footerLabel, 0, Qt.AlignHCenter)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_footerFrame.addItem(self.horizontalSpacer_8)

        self.currentInfoLabel = QLabel(self.footerFrame)
        self.currentInfoLabel.setObjectName(u"currentInfoLabel")
        self.currentInfoLabel.setMaximumWidth(360)

        self.horizontalLayout_footerFrame.addWidget(self.currentInfoLabel)

        self.horizontalSpacer_19 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_footerFrame.addItem(self.horizontalSpacer_19)

        self.githubProfileBtn = QPushButton(self.footerFrame)
        self.githubProfileBtn.setObjectName(u"githubProfileBtn")
        icon37 = QIcon()
        icon37.addFile(u":/icons/icons/github.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.githubProfileBtn.setIcon(icon37)

        self.horizontalLayout_footerFrame.addWidget(
            self.githubProfileBtn, 0, Qt.AlignHCenter)

        self.linkedinProfileBtn = QPushButton(self.footerFrame)
        self.linkedinProfileBtn.setObjectName(u"linkedinProfileBtn")
        icon38 = QIcon()
        icon38.addFile(u":/icons/icons/linkedin.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.linkedinProfileBtn.setIcon(icon38)

        self.horizontalLayout_footerFrame.addWidget(
            self.linkedinProfileBtn, 0, Qt.AlignHCenter)

        self.instagramProfileBtn = QPushButton(self.footerFrame)
        self.instagramProfileBtn.setObjectName(u"instagramProfileBtn")
        icon39 = QIcon()
        icon39.addFile(u":/icons/icons/instagram.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.instagramProfileBtn.setIcon(icon39)

        self.horizontalLayout_footerFrame.addWidget(
            self.instagramProfileBtn, 0, Qt.AlignHCenter)

        # self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # self.horizontalLayout_footerFrame.addItem(self.horizontalSpacer_7)

        self.resizeFrame = QFrame(self.footerFrame)
        self.resizeFrame.setObjectName(u"resizeFrame")
        self.resizeFrame.setFrameShape(QFrame.StyledPanel)
        self.resizeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_resizeFrame = QHBoxLayout(self.resizeFrame)
        self.horizontalLayout_resizeFrame.setSpacing(0)
        self.horizontalLayout_resizeFrame.setObjectName(
            u"horizontalLayout_resizeFrame")
        self.horizontalLayout_resizeFrame.setContentsMargins(0, 0, 2, 2)
        self.resizeIconLabel = QLabel(self.resizeFrame)
        self.resizeIconLabel.setObjectName(u"resizeIconLabel")
        self.resizeIconLabel.setPixmap(
            QPixmap(u":/icons/icons/cil-size-grip.png"))

        self.horizontalLayout_resizeFrame.addWidget(
            self.resizeIconLabel, 0, Qt.AlignBottom)

        self.horizontalLayout_footerFrame.addWidget(self.resizeFrame)

        self.horizontalLayout_footerFrame.setStretch(2, 2)

        self.verticalLayout_footer.addWidget(self.footerFrame)

        self.verticalLayout_mainBodyContainer.addWidget(self.footer)

        self.centralwidgetlayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.imageDownloadThreads = []
        # self.videoDownloadThreads = []
        self.settingHelpMenu.setCurrentIndex(0)
        self.mainAppStack.setCurrentIndex(2)
        self.historyTime = ""
        self.historyElapsed = ""
        self.historyLocation = ""
        self.historyUrl = ""
        self.historyTitle = ""
        self.dots = ""
        self.dots_timer = QTimer(MainWindow)
        self.dots_timer.timeout.connect(self.updateDots)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def addVideos(self, videos, mainWindow):
        self.thumbnailBtnMapsID = {}
        self.redirectBtnMapsID = {}
        self.thumbnailBtnMapsTitle = {}
        self.streamBtnMapsID = {}
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/chrome.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/eye.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/download.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/youtube.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        row, col = 0, 0
        for index, video_info in enumerate(videos):
            self.videoContainer = QWidget(self.videoSpaceFrame)
            self.videoContainer.setObjectName(u"videoContainer")
            sizePolicy.setHeightForWidth(
                self.videoContainer.sizePolicy().hasHeightForWidth())
            self.videoContainer.setSizePolicy(sizePolicy)
            self.videoContainer.setMinimumSize(QSize(360, 284))
            self.videoContainer.setMaximumSize(QSize(640, 442))
            self.videoContainer.setStyleSheet(u"")
            self.verticalLayout_videoContainer = QVBoxLayout(
                self.videoContainer)
            self.verticalLayout_videoContainer.setSpacing(0)
            self.verticalLayout_videoContainer.setObjectName(
                u"verticalLayout_videoContainer")
            self.verticalLayout_videoContainer.setContentsMargins(4, 4, 4, 0)
            self.videoThumbnailFrame = QFrame(self.videoContainer)
            self.videoThumbnailFrame.setObjectName(u"videoThumbnailFrame")
            self.videoThumbnailFrame.setMinimumSize(QSize(0, 0))
            self.videoThumbnailFrame.setMaximumSize(QSize(16777215, 360))
            self.videoThumbnailFrame.setFrameShape(QFrame.StyledPanel)
            self.videoThumbnailFrame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_videoThumbnailFrame = QVBoxLayout(
                self.videoThumbnailFrame)
            self.verticalLayout_videoThumbnailFrame.setSpacing(0)
            self.verticalLayout_videoThumbnailFrame.setObjectName(
                u"verticalLayout_videoThumbnailFrame")
            self.verticalLayout_videoThumbnailFrame.setContentsMargins(
                0, 0, 0, 0)
            self.videoThumbnailBtn = ResizableIconButton(
                self.videoThumbnailFrame)
            self.videoThumbnailBtn.setObjectName(u"videoThumbnailBtn")
            sizePolicy5 = QSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy5.setHorizontalStretch(0)
            sizePolicy5.setVerticalStretch(0)
            sizePolicy5.setHeightForWidth(
                self.videoThumbnailBtn.sizePolicy().hasHeightForWidth())
            self.videoThumbnailBtn.setSizePolicy(sizePolicy5)
            self.videoThumbnailBtn.setMinimumSize(QSize(360, 202))
            self.videoThumbnailBtn.setMaximumSize(QSize(16777215, 360))
            self.videoThumbnailBtn.setCursor(QCursor(Qt.PointingHandCursor))

            self.verticalLayout_videoThumbnailFrame.addWidget(
                self.videoThumbnailBtn)

            self.verticalLayout_videoContainer.addWidget(
                self.videoThumbnailFrame)

            self.videoInfoFrame = QFrame(self.videoContainer)
            self.videoInfoFrame.setObjectName(u"videoInfoFrame")
            self.videoInfoFrame.setMinimumSize(QSize(240, 0))
            self.videoInfoFrame.setMaximumSize(QSize(16777215, 70))
            self.videoInfoFrame.setFrameShape(QFrame.StyledPanel)
            self.videoInfoFrame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_videoInfoFrame = QVBoxLayout(
                self.videoInfoFrame)
            self.verticalLayout_videoInfoFrame.setSpacing(0)
            self.verticalLayout_videoInfoFrame.setObjectName(
                u"verticalLayout_videoInfoFrame")
            self.verticalLayout_videoInfoFrame.setContentsMargins(0, 0, 0, 0)
            self.videoTitleFrame = QFrame(self.videoInfoFrame)
            self.videoTitleFrame.setObjectName(u"videoTitleFrame")
            self.videoTitleFrame.setMinimumSize(QSize(0, 38))
            self.videoTitleFrame.setFrameShape(QFrame.StyledPanel)
            self.videoTitleFrame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_videoTitleFrame = QHBoxLayout(
                self.videoTitleFrame)
            self.horizontalLayout_videoTitleFrame.setSpacing(0)
            self.horizontalLayout_videoTitleFrame.setObjectName(
                u"horizontalLayout_videoTitleFrame")
            self.horizontalLayout_videoTitleFrame.setContentsMargins(
                0, 0, 0, 0)
            self.channelIconBtn = CircularIconButton(self.videoTitleFrame)
            self.channelIconBtn.setObjectName(u"channelIconBtn")
            self.channelIconBtn.setMinimumSize(QSize(28, 28))
            self.channelIconBtn.setMaximumSize(QSize(32, 32))

            self.horizontalLayout_videoTitleFrame.addWidget(
                self.channelIconBtn)

            self.videoTitleLabel = QLabel(self.videoTitleFrame)
            self.videoTitleLabel.setObjectName(u"videoTitleLabel")

            self.horizontalLayout_videoTitleFrame.addWidget(
                self.videoTitleLabel)

            self.videoDurationLabel = QLabel(self.videoTitleFrame)
            self.videoDurationLabel.setObjectName(u"videoDurationLabel")
            self.videoDurationLabel.setMinimumSize(QSize(0, 12))

            self.horizontalLayout_videoTitleFrame.addWidget(
                self.videoDurationLabel, 0, Qt.AlignRight | Qt.AlignTop)

            self.verticalLayout_videoInfoFrame.addWidget(self.videoTitleFrame)

            self.channelFrame = QFrame(self.videoInfoFrame)
            self.channelFrame.setObjectName(u"channelFrame")
            self.channelFrame.setFrameShape(QFrame.StyledPanel)
            self.channelFrame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_channelFrame = QHBoxLayout(self.channelFrame)
            self.horizontalLayout_channelFrame.setSpacing(0)
            self.horizontalLayout_channelFrame.setObjectName(
                u"horizontalLayout_channelFrame")
            self.horizontalLayout_channelFrame.setContentsMargins(0, 0, 0, 0)
            self.channelNameLabel = QLabel(self.channelFrame)
            self.channelNameLabel.setObjectName(u"channelNameLabel")
            self.channelNameLabel.setWordWrap(False)

            self.horizontalLayout_channelFrame.addWidget(self.channelNameLabel)

            self.verticalLayout_videoInfoFrame.addWidget(self.channelFrame)

            self.viewsAgeFrame = QFrame(self.videoInfoFrame)
            self.viewsAgeFrame.setObjectName(u"viewsAgeFrame")
            self.viewsAgeFrame.setFrameShape(QFrame.StyledPanel)
            self.viewsAgeFrame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_viewsAgeFrame = QHBoxLayout(
                self.viewsAgeFrame)
            self.horizontalLayout_viewsAgeFrame.setSpacing(0)
            self.horizontalLayout_viewsAgeFrame.setObjectName(
                u"horizontalLayout_viewsAgeFrame")
            self.horizontalLayout_viewsAgeFrame.setContentsMargins(0, 0, 0, 0)
            self.viewsLabel = QLabel(self.viewsAgeFrame)
            self.viewsLabel.setObjectName(u"viewsLabel")
            self.viewsLabel.setWordWrap(False)

            self.horizontalLayout_viewsAgeFrame.addWidget(self.viewsLabel)

            self.horizontalSpacer_16 = QSpacerItem(
                40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.horizontalLayout_viewsAgeFrame.addItem(
                self.horizontalSpacer_16)

            self.streamBtn = QPushButton(self.viewsAgeFrame)
            self.streamBtn.setObjectName(u"streamBtn")
            self.streamBtn.setMinimumSize(QSize(24, 24))
            self.streamBtn.setMaximumSize(QSize(32, 32))
            self.streamBtn.setCursor(QCursor(Qt.PointingHandCursor))

            self.horizontalLayout_viewsAgeFrame.addWidget(
                self.streamBtn, 0, Qt.AlignRight | Qt.AlignVCenter)

            self.downloadPageRedirectBtn = QPushButton(self.viewsAgeFrame)
            self.downloadPageRedirectBtn.setObjectName(
                u"downloadPageRedirectBtn")
            self.downloadPageRedirectBtn.setMinimumSize(QSize(24, 24))
            self.downloadPageRedirectBtn.setMaximumSize(QSize(32, 32))
            self.downloadPageRedirectBtn.setCursor(
                QCursor(Qt.PointingHandCursor))

            self.horizontalLayout_viewsAgeFrame.addWidget(
                self.downloadPageRedirectBtn, 0, Qt.AlignRight)

            self.verticalLayout_videoInfoFrame.addWidget(
                self.viewsAgeFrame, 0, Qt.AlignTop)

            self.downloadRedirectFrame = QFrame(self.videoInfoFrame)
            self.downloadRedirectFrame.setObjectName(u"downloadRedirectFrame")
            self.downloadRedirectFrame.setFrameShape(QFrame.StyledPanel)
            self.downloadRedirectFrame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_downloadRedirectFrame = QHBoxLayout(
                self.downloadRedirectFrame)
            self.horizontalLayout_downloadRedirectFrame.setSpacing(0)
            self.horizontalLayout_downloadRedirectFrame.setObjectName(
                u"horizontalLayout_downloadRedirectFrame")
            self.horizontalLayout_downloadRedirectFrame.setContentsMargins(
                0, 0, 0, 0)

            self.verticalLayout_videoInfoFrame.addWidget(
                self.downloadRedirectFrame)

            self.verticalLayout_videoInfoFrame.setStretch(1, 2)
            self.verticalLayout_videoInfoFrame.setStretch(2, 2)

            self.verticalLayout_videoContainer.addWidget(self.videoInfoFrame)

            try:
                thumbnailDownloader = ImageDownloader(
                    video_info['thumbnail'], self.videoThumbnailBtn)
                thumbnailDownloader.imageDownloaded.connect(self.setImage)
                thumbnailDownloader.start()
                self.imageDownloadThreads.append(thumbnailDownloader)

                channelIconDownloader = ImageDownloader(
                    video_info['channel_icon'], self.channelIconBtn)
                channelIconDownloader.imageDownloaded.connect(self.setImage)
                channelIconDownloader.start()
                self.imageDownloadThreads.append(channelIconDownloader)

            except Exception as e:
                self.imageDownloadThreads.clear()
                print("Error due to: ", e)
                self.videoThumbnailBtn.setIcon(icon11)
                self.channelIconBtn.setIcon(icon19)
                self.videoThumbnailBtn.setIconSize(QSize(202, 202))
                self.channelIconBtn.setIconSize(QSize(30, 30))

            self.streamBtn.setIcon(icon20)
            self.downloadPageRedirectBtn.setIcon(icon21)
            self.streamBtn.setIconSize(QSize(24, 24))
            self.downloadPageRedirectBtn.setIconSize(QSize(24, 24))

            self.thumbnailBtnMapsID[self.videoThumbnailBtn] = video_info['id']
            self.redirectBtnMapsID[self.downloadPageRedirectBtn] = video_info['id']
            self.streamBtnMapsID[self.streamBtn] = video_info['id']
            self.thumbnailBtnMapsTitle[self.videoThumbnailBtn] = video_info['title']
            self.videoThumbnailBtn.clicked.connect(
                lambda _, id=video_info['id'], title=video_info['title']: mainWindow.handleThumbnailBtnClick(id, title))
            self.downloadPageRedirectBtn.clicked.connect(
                lambda _, id=video_info['id'], title=video_info['title']: mainWindow.handleDownloadBtnClick(id, title))
            self.streamBtn.clicked.connect(
                lambda _, id=video_info['id'], title=video_info['title']: mainWindow.handleStreamBtnClick(id, title))
            self.videoThumbnailBtn.setText("")
            self.downloadPageRedirectBtn.setText("")
            self.downloadPageRedirectBtn.setToolTip(
                QCoreApplication.translate("MainWindow", u"Redirects To Download Window", None))
            self.streamBtn.setText("")
            self.channelIconBtn.setText("")
            # self.gridLayout_videoSpaceFrame.addWidget(self.videoContainer)#################################################
            self.videoThumbnailBtn.setToolTip(
                QCoreApplication.translate("MainWindow", u"Downloads Directly With Default Parameters", None))
            self.videoTitleLabel.setText(QCoreApplication.translate(
                "MainWindow", video_info['title'], None))
            self.channelNameLabel.setText(QCoreApplication.translate(
                "MainWindow", video_info['channel'], None))
            self.viewsLabel.setText(
                QCoreApplication.translate("MainWindow", f"{video_info['views']} • {video_info['time']}", None))
            self.videoDurationLabel.setText(QCoreApplication.translate(
                "MainWindow", video_info['duration'], None))
            self.downloadPageRedirectBtn.setToolTip(
                QCoreApplication.translate("MainWindow", u"Redirects To Download Window", None))
            self.streamBtn.setToolTip(QCoreApplication.translate(
                "MainWindow", u"Plays the Video Online", None))
            self.gridLayout_videoSpaceFrame.addWidget(
                self.videoContainer, row, col, 1, 1)
            col += 1
            if col == 3:
                col = 0
                row += 1

    def setImage(self, pixmap, button):
        button.setIcon(QIcon(pixmap))
        button.setIconSize(button.size())

    def stopImageDownloaderThreads(self):
        for thread in self.imageDownloadThreads:
            thread.stop()
            thread.wait()
            thread.deleteLater()
            print("Deleting Image Downloader Threads")
        self.imageDownloadThreads.clear()

    def addDownload(self, id, title, mainWindow, direct=False):
        try:
            self.verticalLayout_downloadsAreaWidget.removeWidget(
                self.homeRedirectBtn)
            self.verticalLayout_downloadsAreaWidget.removeItem(
                self.downloadSpacer)
            self.homeRedirectBtn.deleteLater()
            del self.downloadSpacer
        except:
            pass
        self.downloadBtnMapsID = {}
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.downloadItemFrame = QFrame(self.downloadsAreaWidget)
        self.downloadItemFrame.setObjectName(u"downloadItemFrame")
        sizePolicy.setHeightForWidth(
            self.downloadItemFrame.sizePolicy().hasHeightForWidth())
        self.downloadItemFrame.setSizePolicy(sizePolicy)
        self.downloadItemFrame.setMinimumSize(QSize(0, 85))
        self.downloadItemFrame.setMaximumSize(QSize(16777215, 120))
        self.downloadItemFrame.setStyleSheet(u"")
        self.downloadItemFrame.setFrameShape(QFrame.StyledPanel)
        self.downloadItemFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_downloadItemFrame = QVBoxLayout(
            self.downloadItemFrame)
        self.verticalLayout_downloadItemFrame.setSpacing(0)
        self.verticalLayout_downloadItemFrame.setObjectName(
            u"verticalLayout_downloadItemFrame")
        self.verticalLayout_downloadItemFrame.setContentsMargins(3, 3, 3, 3)
        self.downloadMediaTitleLabel = QLabel(self.downloadItemFrame)
        self.downloadMediaTitleLabel.setObjectName(u"downloadMediaTitleLabel")

        self.verticalLayout_downloadItemFrame.addWidget(
            self.downloadMediaTitleLabel)

        self.qualitySelectWidget = QWidget(self.downloadItemFrame)
        self.qualitySelectWidget.setObjectName(u"qualitySelectWidget")
        self.qualitySelectWidget.setMinimumSize(QSize(0, 28))
        self.qualitySelectWidget.setStyleSheet(u"")
        self.horizontalLayout_qualitySelectWidget = QHBoxLayout(
            self.qualitySelectWidget)
        self.horizontalLayout_qualitySelectWidget.setSpacing(0)
        self.horizontalLayout_qualitySelectWidget.setObjectName(
            u"horizontalLayout_qualitySelectWidget")
        self.horizontalLayout_qualitySelectWidget.setContentsMargins(
            4, 0, 4, 0)
        self.video4kRadioBtn = QRadioButton(self.qualitySelectWidget)
        self.video4kRadioBtn.setObjectName(u"video4kRadioBtn")

        self.horizontalLayout_qualitySelectWidget.addWidget(
            self.video4kRadioBtn)

        self.video1080pRadioBtn = QRadioButton(self.qualitySelectWidget)
        self.video1080pRadioBtn.setObjectName(u"video1080pRadioBtn")

        self.horizontalLayout_qualitySelectWidget.addWidget(
            self.video1080pRadioBtn)

        self.video720pRadioBtn = QRadioButton(self.qualitySelectWidget)
        self.video720pRadioBtn.setObjectName(u"video720pRadioBtn")

        self.horizontalLayout_qualitySelectWidget.addWidget(
            self.video720pRadioBtn)

        self.audio192kbpsRadioBtn = QRadioButton(self.qualitySelectWidget)
        self.audio192kbpsRadioBtn.setObjectName(u"audio192kbpsRadioBtn")

        self.horizontalLayout_qualitySelectWidget.addWidget(
            self.audio192kbpsRadioBtn)

        self.audio320kbpsRadioBtn = QRadioButton(self.qualitySelectWidget)
        self.audio320kbpsRadioBtn.setObjectName(u"audio320kbpsRadioBtn")

        self.horizontalLayout_qualitySelectWidget.addWidget(
            self.audio320kbpsRadioBtn)

        self.downloadBtn = QPushButton(self.qualitySelectWidget)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setMaximumWidth(120)

        self.horizontalLayout_qualitySelectWidget.addWidget(self.downloadBtn)

        self.verticalLayout_downloadItemFrame.addWidget(
            self.qualitySelectWidget)

        self.downloadProgressFrame = QFrame(self.downloadItemFrame)
        self.downloadProgressFrame.setObjectName(u"downloadProgressFrame")
        self.downloadProgressFrame.setStyleSheet(u"")
        self.downloadProgressFrame.setFrameShape(QFrame.StyledPanel)
        self.downloadProgressFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_downloadProgressFrame = QHBoxLayout(
            self.downloadProgressFrame)
        self.horizontalLayout_downloadProgressFrame.setSpacing(8)
        self.horizontalLayout_downloadProgressFrame.setObjectName(
            u"horizontalLayout_downloadProgressFrame")
        self.horizontalLayout_downloadProgressFrame.setContentsMargins(
            4, 0, 4, 0)
        self.currentDownloadedLabel = QLabel(self.downloadProgressFrame)
        self.currentDownloadedLabel.setObjectName(u"currentDownloadedLabel")
        self.currentDownloadedLabel.setMinimumSize(QSize(72, 0))
        self.currentDownloadedLabel.setMaximumSize(QSize(72, 64))
        self.currentDownloadedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_downloadProgressFrame.addWidget(
            self.currentDownloadedLabel)

        self.downloadProgressSlider = QSlider(self.downloadProgressFrame)
        self.downloadProgressSlider.setObjectName(u"downloadProgressSlider")
        self.downloadProgressSlider.setMinimumSize(QSize(240, 0))
        self.downloadProgressSlider.setFocusPolicy(Qt.NoFocus)
        self.downloadProgressSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_downloadProgressFrame.addWidget(
            self.downloadProgressSlider)

        self.downloadSizeLabel = QLabel(self.downloadProgressFrame)
        self.downloadSizeLabel.setObjectName(u"downloadSizeLabel")
        self.downloadSizeLabel.setMinimumSize(QSize(72, 0))
        self.downloadSizeLabel.setMaximumSize(QSize(72, 64))
        self.downloadSizeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_downloadProgressFrame.addWidget(
            self.downloadSizeLabel)

        self.etaLabel = QLabel(self.downloadProgressFrame)
        self.etaLabel.setObjectName(u"etaLabel")
        self.etaLabel.setMinimumSize(QSize(86, 0))
        self.etaLabel.setMaximumSize(QSize(86, 16777215))
        self.etaLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_downloadProgressFrame.addWidget(self.etaLabel)

        self.elapsedTimeLabel = QLabel(self.downloadProgressFrame)
        self.elapsedTimeLabel.setObjectName(u"elapsedTimeLabel")
        self.elapsedTimeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_downloadProgressFrame.addWidget(
            self.elapsedTimeLabel)

        self.downloadPause = QPushButton(self.downloadProgressFrame)
        self.downloadPause.setObjectName(u"downloadPause")
        self.downloadPause.setMinimumSize(QSize(72, 0))

        self.horizontalLayout_downloadProgressFrame.addWidget(
            self.downloadPause)

        self.verticalLayout_downloadItemFrame.addWidget(
            self.downloadProgressFrame)

        self.verticalLayout_downloadsAreaWidget.addWidget(
            self.downloadItemFrame)

        self.downloadMediaTitleLabel.setText(
            QCoreApplication.translate("MainWindow", f"{title}", None))
        self.video4kRadioBtn.setText(
            QCoreApplication.translate("MainWindow", u"4k Video", None))
        self.video1080pRadioBtn.setText(
            QCoreApplication.translate("MainWindow", u"1080p Video", None))
        self.video720pRadioBtn.setText(
            QCoreApplication.translate("MainWindow", u"720p Video", None))
        self.audio192kbpsRadioBtn.setText(
            QCoreApplication.translate("MainWindow", u"192kbps Audio", None))
        self.audio320kbpsRadioBtn.setText(
            QCoreApplication.translate("MainWindow", u"320kbps Audio", None))
        self.downloadBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Downloads The Selected Video", None))
        self.downloadBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Download", None))
        self.currentDownloadedLabel.setText(
            QCoreApplication.translate("MainWindow", u"0B", None))
        self.downloadSizeLabel.setText(
            QCoreApplication.translate("MainWindow", u"0B", None))
        self.etaLabel.setText(QCoreApplication.translate(
            "MainWindow", u"ETA: 00:00", None))
        self.elapsedTimeLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Elapsed: 00:00", None))
        self.downloadPause.setText(
            QCoreApplication.translate("MainWindow", u"Pause", None))
        if direct:
            self.video1080pRadioBtn.setChecked(True)
            self.startDownload(id, self.downloadPause, mainWindow, True)
        else:
            self.downloadBtnMapsID[self.downloadBtn] = id
            self.downloadBtn.clicked.connect(
                lambda: self.startDownload(id, self.downloadPause, mainWindow))
        self.downloadPause.setEnabled(True)
        self.historyTitle = title
        self.homeRedirect()
        self.mainAppStack.setCurrentIndex(3)

    def startDownload(self, video_id, start_pause_btn, mainWindow, default_type=False):
        if not default_type:
            if self.video4kRadioBtn.isChecked():
                type = 5
            elif self.video1080pRadioBtn.isChecked():
                type = 4
            elif self.video720pRadioBtn.isChecked():
                type = 3
            elif self.audio320kbpsRadioBtn.isChecked():
                type = 2
            elif self.audio192kbpsRadioBtn.isChecked():
                type = 1
            else:
                mainWindow.pushNotification("Select a Downlaod Type!")
                return
        else:
            type = 4
        self.historyUrl = f"https://www.youtube.com/watch?v={video_id}"
        self.historyLocation = mainWindow.default_download_directory
        self.video4kRadioBtn.setEnabled(False)
        self.video1080pRadioBtn.setEnabled(False)
        self.video720pRadioBtn.setEnabled(False)
        self.audio320kbpsRadioBtn.setEnabled(False)
        self.audio192kbpsRadioBtn.setEnabled(False)
        self.downloadBtn.setEnabled(False)
        self.download_thread = DownloadThread(video_id, type, mainWindow.default_download_directory,
                                              mainWindow.default_audio_extension, mainWindow.default_video_extension,
                                              mainWindow)
        self.download_thread.progress.connect(
            lambda progress_info: self.getProgress(progress_info))
        self.download_thread.status.connect(
            lambda text: self.updateStatus(text, mainWindow))
        self.download_thread.start()
        mainWindow.pushNotification("Download Will Start Shortly!")
        start_pause_btn.clicked.connect(self.download_thread.toggle_pause)

    def getProgress(self, progress_info):
        self.internetSpeedLabel.setText(progress_info['speed'])
        self.downloadProgressSlider.setValue(int(progress_info['progress']))
        self.currentDownloadedLabel.setText(progress_info['downloaded'])
        self.downloadSizeLabel.setText(progress_info['size'])
        self.etaLabel.setText(f"ETA: {(progress_info['eta'])}")
        self.elapsedTimeLabel.setText(f"Elapsed: {progress_info['elapsed']}")

    def updateStatus(self, text, mainWindow):
        if text == 'ERROR':
            mainWindow.pushNotification("Download Error!")
            self.downloadBtn.setText("ERROR!")

        if text == 'Finished':
            mainWindow.playSound('sound/cat.wav', 50)
            self.historyElapsed = self.elapsedTimeLabel.text()[9:]
            self.historyTime = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
            mainWindow.history_list = mainWindow.history_manager.add_history(self.historyTime, self.historyElapsed,
                                                                             self.historyLocation, self.historyUrl,
                                                                             self.historyTitle)
            try:
                self.thumbnailBtnMapsID.clear()
                self.redirectBtnMapsID.clear()
                self.thumbnailBtnMapsTitle.clear()
                self.streamBtnMapsID.clear()
                self.downloadBtnMapsID.clear()
            except AttributeError as e:
                print("No Search has been done!")
            self.addHistory(mainWindow.history_list)
            self.downloadPause.setEnabled(False)
            self.download_thread.stop()
            self.download_thread.wait()
            self.download_thread.deleteLater()
            # QTimer.singleShot(500, lambda: mainWindow.file_watcher_system.directory_changed(path=None))
            self.dots_timer.stop()
            self.downloadBtn.setText("Downloaded!")
            mainWindow.pushNotification("Downloaded!")
            self.internetSpeedLabel.setText("0 B")
            self.mainAppStack.setCurrentIndex(4)

        if text == 'Pause':
            self.downloadPause.setText("Resume")

        elif text == 'Resume':
            self.downloadPause.setText("Pause")

        elif text == 'Downloading':
            if not self.dots_timer.isActive():
                self.dots_timer.start(500)

    def updateDots(self):
        if len(self.dots) < 3:
            self.dots += "."
        else:
            self.dots = ""
        self.downloadBtn.setText(f"Downloading{self.dots}")

    def homeRedirect(self):
        self.homeRedirectBtn = QPushButton(self.downloadsAreaWidget)
        self.homeRedirectBtn.setObjectName(u"homeRedirectBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.homeRedirectBtn.sizePolicy().hasHeightForWidth())
        self.homeRedirectBtn.setSizePolicy(sizePolicy6)
        self.homeRedirectBtn.setMinimumSize(QSize(0, 85))
        self.homeRedirectBtn.setMaximumSize(QSize(16777215, 120))
        self.homeRedirectBtn.setStyleSheet(u"")

        self.verticalLayout_downloadsAreaWidget.addWidget(self.homeRedirectBtn)

        self.downloadSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_downloadsAreaWidget.addItem(self.downloadSpacer)
        self.homeRedirectBtn.setText(QCoreApplication.translate(
            "MainWindow", u"No More Active Download Tasks!", None))
        self.homeRedirectBtn.clicked.connect(
            lambda: self.mainAppStack.setCurrentIndex(0))

    def addFiles(self, mainWindow, file_info):
        try:
            def convert_size(size_bytes):
                if size_bytes == 0:
                    return "0 B"
                size_name = ("B", "KB", "MB", "GB", "TB",
                             "PB", "EB", "ZB", "YB")
                i = int(math.floor(math.log(size_bytes, 1024)))
                p = math.pow(1024, i)
                s = round(size_bytes / p, 2)
                return f"{s} {size_name[i]}"

            self.filePlayBtnMapsFile = {}
            sizePolicy = QSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            for i in reversed(range(self.verticalLayout_filesScrollAreaContents.count())):
                item = self.verticalLayout_filesScrollAreaContents.itemAt(i)
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    self.verticalLayout_filesScrollAreaContents.removeWidget(
                        widget_to_remove)
                    widget_to_remove.setParent(None)
                else:
                    self.verticalLayout_filesScrollAreaContents.removeItem(
                        item)
            for file in file_info:
                self.files = QFrame(self.filesScrollAreaContents)
                self.files.setObjectName(u"files")
                sizePolicy.setHeightForWidth(
                    self.files.sizePolicy().hasHeightForWidth())
                self.files.setSizePolicy(sizePolicy)
                self.files.setMinimumSize(QSize(0, 85))
                self.files.setMaximumSize(QSize(16777215, 120))
                self.files.setStyleSheet(u"")
                self.verticalLayout_files = QVBoxLayout(self.files)
                self.verticalLayout_files.setSpacing(0)
                self.verticalLayout_files.setObjectName(
                    u"verticalLayout_files")
                self.verticalLayout_files.setContentsMargins(0, 0, 0, 0)
                self.fileTitleFrame = QFrame(self.files)
                self.fileTitleFrame.setObjectName(u"fileTitleFrame")
                sizePolicy.setHeightForWidth(
                    self.fileTitleFrame.sizePolicy().hasHeightForWidth())
                self.fileTitleFrame.setSizePolicy(sizePolicy)
                self.fileTitleFrame.setFrameShape(QFrame.StyledPanel)
                self.fileTitleFrame.setFrameShadow(QFrame.Raised)
                self.verticalLayout_fileTitleFrame = QVBoxLayout(
                    self.fileTitleFrame)
                self.verticalLayout_fileTitleFrame.setSpacing(0)
                self.verticalLayout_fileTitleFrame.setObjectName(
                    u"verticalLayout_fileTitleFrame")
                self.verticalLayout_fileTitleFrame.setContentsMargins(
                    0, 0, 0, 0)
                self.fileTitleLabel = ElidedLabel(self.fileTitleFrame)
                self.fileTitleLabel.setObjectName(u"fileTitleLabel")
                self.fileTitleLabel.setMinimumSize(QSize(0, 0))
                self.fileTitleLabel.setStyleSheet(u"")
                self.fileTitleLabel.setWordWrap(False)

                self.verticalLayout_fileTitleFrame.addWidget(
                    self.fileTitleLabel)

                self.fileInfoFrame = QFrame(self.fileTitleFrame)
                self.fileInfoFrame.setObjectName(u"fileInfoFrame")
                self.fileInfoFrame.setMinimumSize(QSize(0, 26))
                self.fileInfoFrame.setMaximumSize(QSize(16777215, 16777215))
                self.fileInfoFrame.setFrameShape(QFrame.StyledPanel)
                self.fileInfoFrame.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_fileInfoFrame = QHBoxLayout(
                    self.fileInfoFrame)
                self.horizontalLayout_fileInfoFrame.setSpacing(0)
                self.horizontalLayout_fileInfoFrame.setObjectName(
                    u"horizontalLayout_fileInfoFrame")
                self.horizontalLayout_fileInfoFrame.setContentsMargins(
                    0, 0, 0, 0)
                self.fileSizeLabel = QLabel(self.fileInfoFrame)
                self.fileSizeLabel.setObjectName(u"fileSizeLabel")
                self.fileSizeLabel.setMinimumSize(QSize(120, 0))

                self.horizontalLayout_fileInfoFrame.addWidget(
                    self.fileSizeLabel)

                self.horizontalSpacer_18 = QSpacerItem(
                    40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_fileInfoFrame.addItem(
                    self.horizontalSpacer_18)

                self.fileExtensionLabel = QLabel(self.fileInfoFrame)
                self.fileExtensionLabel.setObjectName(u"fileExtensionLabel")
                self.fileExtensionLabel.setMinimumSize(QSize(120, 0))

                self.horizontalLayout_fileInfoFrame.addWidget(
                    self.fileExtensionLabel)

                self.horizontalSpacer_15 = QSpacerItem(
                    40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_fileInfoFrame.addItem(
                    self.horizontalSpacer_15)

                self.horizontalLayout_fileInfoFrame.setStretch(1, 1)
                self.horizontalLayout_fileInfoFrame.setStretch(3, 4)

                self.verticalLayout_fileTitleFrame.addWidget(
                    self.fileInfoFrame)

                self.verticalLayout_files.addWidget(self.fileTitleFrame)

                self.fileTypeFrame = QFrame(self.files)
                self.fileTypeFrame.setObjectName(u"fileTypeFrame")
                self.fileTypeFrame.setMinimumSize(QSize(0, 34))
                self.fileTypeFrame.setMaximumSize(QSize(16777215, 16777215))
                self.fileTypeFrame.setFrameShape(QFrame.StyledPanel)
                self.fileTypeFrame.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_fileTypeFrame = QHBoxLayout(
                    self.fileTypeFrame)
                self.horizontalLayout_fileTypeFrame.setSpacing(0)
                self.horizontalLayout_fileTypeFrame.setObjectName(
                    u"horizontalLayout_fileTypeFrame")
                self.horizontalLayout_fileTypeFrame.setContentsMargins(
                    0, 0, 0, 0)
                self.filePlayBtn = QPushButton(self.fileTypeFrame)
                self.filePlayBtn.setObjectName(u"filePlayBtn")
                self.filePlayBtn.setMinimumSize(QSize(35, 35))
                icon23 = QIcon()
                icon23.addFile(u":/icons/icons/play.svg",
                               QSize(), QIcon.Normal, QIcon.Off)
                self.filePlayBtn.setIcon(icon23)
                self.filePlayBtn.setIconSize(QSize(30, 30))

                self.horizontalLayout_fileTypeFrame.addWidget(self.filePlayBtn)

                self.fileTypeLabel = QLabel(self.fileTypeFrame)
                self.fileTypeLabel.setObjectName(u"fileTypeLabel")
                self.fileTypeLabel.setStyleSheet(u"")

                self.horizontalLayout_fileTypeFrame.addWidget(
                    self.fileTypeLabel, 0, Qt.AlignLeft)

                self.horizontalSpacer_17 = QSpacerItem(
                    40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_fileTypeFrame.addItem(
                    self.horizontalSpacer_17)

                self.fileTimeLabel = QLabel(self.fileTypeFrame)
                self.fileTimeLabel.setObjectName(u"fileTimeLabel")

                self.horizontalLayout_fileTypeFrame.addWidget(
                    self.fileTimeLabel)

                self.verticalLayout_files.addWidget(
                    self.fileTypeFrame, 0, Qt.AlignLeft)

                self.verticalLayout_filesScrollAreaContents.addWidget(
                    self.files)

                self.filePlayBtn.setText("")
                self.filePlayBtnMapsFile[self.filePlayBtn] = file['path']
                self.filePlayBtn.clicked.connect(
                    lambda _, path=file['path']: mainWindow.handlefilePlayBtnClick(path))
                self.filePlayBtn.setText("")
                self.fileSizeLabel.setText(
                    f"File Size: {convert_size(int(file['size']))}")
                self.fileExtensionLabel.setText(
                    f"File Extension: {str(file['type'])}")
                try:
                    if file['type'] not in (mainWindow.audio_formats + mainWindow.video_formats):
                        self.filePlayBtn.hide()
                    if file['type'].lower() in mainWindow.audio_formats:
                        file['type'] = "Audio"
                        mainWindow.media_files.append(file['path'])
                    elif file['type'].lower() in mainWindow.video_formats:
                        file['type'] = "Video"
                        mainWindow.media_files.append(file['path'])
                    else:
                        file['type'] = f"{file['type'][1:].upper()} File"
                except Exception as e:
                    print("Error due to: ", e)
                    mainWindow.pushNotification(
                        f"Error While Sorting Media Files from File Type. {e}")
                self.fileTypeLabel.setText(str(file["type"]))
                self.fileTitleLabel.setText(file['name'])
                self.fileTimeLabel.setText(
                    "Last Modified: %s" % datetime.fromtimestamp(int(file['time'])).strftime("%H:%M:%S %d-%m-%Y"))
                self.filePlayBtn.setToolTip(
                    QCoreApplication.translate("MainWindow", u"Redirects Current File To Media Player", None))
            self.endOfFile()
        except Exception as e:
            print("Error occured in self.addFiles() due to: ", e)
            mainWindow.pushNotification(
                f"Internal Error Occured in self.addFiles() Due to: {e}")

    def endOfFile(self):
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        try:
            self.filePlayBtnMapsFile.clear()
        except Exception as e:
            print(
                "Attribute Error Due to No Files Found! or Empty Files List! Exception: ", e)
        self.endOfFilesBtn = QPushButton(self.filesScrollAreaContents)
        self.endOfFilesBtn.setObjectName(u"endOfFilesBtn")
        sizePolicy.setHeightForWidth(
            self.endOfFilesBtn.sizePolicy().hasHeightForWidth())
        self.endOfFilesBtn.setSizePolicy(sizePolicy)
        self.endOfFilesBtn.setMinimumSize(QSize(0, 85))
        self.endOfFilesBtn.setMaximumSize(QSize(16777215, 120))
        self.endOfFilesBtn.setStyleSheet(u"")

        self.verticalLayout_filesScrollAreaContents.addWidget(
            self.endOfFilesBtn)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_filesScrollAreaContents.addItem(
            self.verticalSpacer_3)

        self.endOfFilesBtn.setText(QCoreApplication.translate(
            "MainWindow", u"End of the Folder! :-(", None))
        self.endOfFilesBtn.clicked.connect(
            lambda: self.mainAppStack.setCurrentIndex(0))

    def addHistory(self, history_list):
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        while self.verticalLayout_historyScrollContent.count():
            child = self.verticalLayout_historyScrollContent.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for history_item in history_list:
            self.historyItem = QFrame(self.historyScrollContent)
            self.historyItem.setObjectName(u"historyItem")
            sizePolicy.setHeightForWidth(
                self.historyItem.sizePolicy().hasHeightForWidth())
            self.historyItem.setSizePolicy(sizePolicy)
            self.historyItem.setMinimumSize(QSize(0, 85))
            self.historyItem.setMaximumSize(QSize(16777215, 120))
            self.historyItem.setStyleSheet(u"")
            self.historyItem.setFrameShape(QFrame.StyledPanel)
            self.historyItem.setFrameShadow(QFrame.Raised)
            self.verticalLayout_historyItem = QVBoxLayout(self.historyItem)
            self.verticalLayout_historyItem.setSpacing(0)
            self.verticalLayout_historyItem.setObjectName(
                u"verticalLayout_historyItem")
            self.verticalLayout_historyItem.setContentsMargins(0, 0, 0, 0)
            self.titleHistoryItemFrame = QFrame(self.historyItem)
            self.titleHistoryItemFrame.setObjectName(u"titleHistoryItemFrame")
            self.titleHistoryItemFrame.setFrameShape(QFrame.StyledPanel)
            self.titleHistoryItemFrame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_titleHistoryItemFrame = QVBoxLayout(
                self.titleHistoryItemFrame)
            self.verticalLayout_titleHistoryItemFrame.setSpacing(0)
            self.verticalLayout_titleHistoryItemFrame.setObjectName(
                u"verticalLayout_titleHistoryItemFrame")
            self.verticalLayout_titleHistoryItemFrame.setContentsMargins(
                0, 0, 0, 0)
            self.titleHistoryItemLabel = QLabel(self.titleHistoryItemFrame)
            self.titleHistoryItemLabel.setObjectName(u"titleHistoryItemLabel")
            self.titleHistoryItemLabel.setStyleSheet(u"")

            self.verticalLayout_titleHistoryItemFrame.addWidget(
                self.titleHistoryItemLabel)

            self.verticalLayout_historyItem.addWidget(
                self.titleHistoryItemFrame)

            self.historyInfoFrame = QFrame(self.historyItem)
            self.historyInfoFrame.setObjectName(u"historyInfoFrame")
            self.historyInfoFrame.setMaximumSize(QSize(16777215, 16777215))
            self.historyInfoFrame.setFrameShape(QFrame.StyledPanel)
            self.historyInfoFrame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_historyInfoFrame = QVBoxLayout(
                self.historyInfoFrame)
            self.verticalLayout_historyInfoFrame.setSpacing(0)
            self.verticalLayout_historyInfoFrame.setObjectName(
                u"verticalLayout_historyInfoFrame")
            self.verticalLayout_historyInfoFrame.setContentsMargins(0, 0, 0, 0)
            self.urlHistoryItemLabel = QLabel(self.historyInfoFrame)
            self.urlHistoryItemLabel.setObjectName(u"urlHistoryItemLabel")
            self.urlHistoryItemLabel.setStyleSheet(u"")

            self.verticalLayout_historyInfoFrame.addWidget(
                self.urlHistoryItemLabel)

            self.historyMetaFrame = QFrame(self.historyInfoFrame)
            self.historyMetaFrame.setObjectName(u"historyMetaFrame")
            self.historyMetaFrame.setFrameShape(QFrame.StyledPanel)
            self.historyMetaFrame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_historyMetaFrame = QHBoxLayout(
                self.historyMetaFrame)
            self.horizontalLayout_historyMetaFrame.setSpacing(0)
            self.horizontalLayout_historyMetaFrame.setObjectName(
                u"horizontalLayout_historyMetaFrame")
            self.horizontalLayout_historyMetaFrame.setContentsMargins(
                0, 0, 0, 0)
            self.historyTimeDateLabel = QLabel(self.historyMetaFrame)
            self.historyTimeDateLabel.setObjectName(u"historyTimeDateLabel")

            self.horizontalLayout_historyMetaFrame.addWidget(
                self.historyTimeDateLabel)

            self.historyTimeElapsedLabel = QLabel(self.historyMetaFrame)
            self.historyTimeElapsedLabel.setObjectName(
                u"historyTimeElapsedLabel")
            self.historyTimeElapsedLabel.setMaximumSize(QSize(160, 16777215))

            self.horizontalLayout_historyMetaFrame.addWidget(
                self.historyTimeElapsedLabel)

            self.historyLocationLabel = QLabel(self.historyMetaFrame)
            self.historyLocationLabel.setObjectName(u"historyLocationLabel")

            self.horizontalLayout_historyMetaFrame.addWidget(
                self.historyLocationLabel)

            self.verticalLayout_historyInfoFrame.addWidget(
                self.historyMetaFrame)

            self.verticalLayout_historyItem.addWidget(self.historyInfoFrame)

            self.verticalLayout_historyScrollContent.addWidget(
                self.historyItem)

            self.titleHistoryItemLabel.setText(QCoreApplication.translate(
                "MainWindow", history_item['title'], None))
            self.urlHistoryItemLabel.setText(
                QCoreApplication.translate("MainWindow", f"URL: {history_item['url']}", None))
            self.historyTimeDateLabel.setText(
                QCoreApplication.translate("MainWindow", f"Time and Date: {history_item['time']}", None))
            self.historyTimeElapsedLabel.setText(
                QCoreApplication.translate("MainWindow", f"Time Elapsed: {history_item['elapsed']}", None))
            self.historyLocationLabel.setText(
                QCoreApplication.translate("MainWindow", f"Location: {history_item['path']}", None))

        self.noMoreHistory()

    def noMoreHistory(self):
        self.historyLastItemFrame = QFrame(self.historyScrollContent)
        self.historyLastItemFrame.setObjectName(u"historyLastItemFrame")
        self.historyLastItemFrame.setMinimumSize(QSize(0, 85))
        self.historyLastItemFrame.setMaximumSize(QSize(16777215, 120))
        self.historyLastItemFrame.setStyleSheet(u"")
        self.historyLastItemFrame.setFrameShape(QFrame.StyledPanel)
        self.historyLastItemFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_historyLastItemFrame = QVBoxLayout(
            self.historyLastItemFrame)
        self.verticalLayout_historyLastItemFrame.setSpacing(0)
        self.verticalLayout_historyLastItemFrame.setObjectName(
            u"verticalLayout_historyLastItemFrame")
        self.verticalLayout_historyLastItemFrame.setContentsMargins(0, 0, 0, 0)
        self.noMoreHistoryBtn = QPushButton(self.historyLastItemFrame)
        self.noMoreHistoryBtn.setObjectName(u"noMoreHistoryBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.noMoreHistoryBtn.sizePolicy().hasHeightForWidth())
        self.noMoreHistoryBtn.setSizePolicy(sizePolicy6)
        self.noMoreHistoryBtn.setMinimumSize(QSize(0, 85))
        self.noMoreHistoryBtn.setMaximumSize(QSize(16777215, 16777215))
        self.noMoreHistoryBtn.setStyleSheet(u"")

        self.verticalLayout_historyLastItemFrame.addWidget(
            self.noMoreHistoryBtn)

        self.verticalLayout_historyScrollContent.addWidget(
            self.historyLastItemFrame)

        self.historySpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_historyScrollContent.addItem(self.historySpacer)

        self.noMoreHistoryBtn.setText(QCoreApplication.translate(
            "MainWindow", u"No More Histories! :-)", None))
        self.noMoreHistoryBtn.clicked.connect(
            lambda: self.mainAppStack.setCurrentIndex(0))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"QTube: Downloader & Player", None))
        # if QT_CONFIG(tooltip)
        self.menuToggleBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Toggle Menu Bar", None))
        # endif // QT_CONFIG(tooltip)
        self.menuToggleBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.homeMenuBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go To Search Window", None))
        # endif // QT_CONFIG(tooltip)
        self.homeMenuBtn.setText(QCoreApplication.translate(
            "MainWindow", u"   Home", None))
        # if QT_CONFIG(tooltip)
        self.downloadMenuBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go To Downloads Window", None))
        # endif // QT_CONFIG(tooltip)
        self.downloadMenuBtn.setText(QCoreApplication.translate(
            "MainWindow", u"   Downloads", None))
        # if QT_CONFIG(tooltip)
        self.fileMenuBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go To Files And Media Player", None))
        # endif // QT_CONFIG(tooltip)
        self.fileMenuBtn.setText(QCoreApplication.translate(
            "MainWindow", u"   Files", None))
        # if QT_CONFIG(tooltip)
        self.historyMenuBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go To History Window", None))
        # endif // QT_CONFIG(tooltip)
        self.historyMenuBtn.setText(QCoreApplication.translate(
            "MainWindow", u"   History", None))
        # if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go To Settings", None))
        # endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"   Settings", None))
        # if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go To Help Menu", None))
        # endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate(
            "MainWindow", u"   Help", None))
        self.settingMenuLabel.setText(
            QCoreApplication.translate("MainWindow", u"Settings", None))
        # if QT_CONFIG(tooltip)
        self.closeSettingMenuBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close Setting Menu", None))
        # endif // QT_CONFIG(tooltip)
        self.closeSettingMenuBtn.setText("")
        self.settingDefaultFolderLabel.setText(
            QCoreApplication.translate("MainWindow", u"Select Download Folder", None))
        # if QT_CONFIG(tooltip)
        self.folderSelectBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Selects Download Folder", None))
        # endif // QT_CONFIG(tooltip)
        self.folderSelectBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Folder Selector", None))
        self.settingVideoExtensionLabel.setText(
            QCoreApplication.translate("MainWindow", u"Default Video Extension", None))
        self.videoExtensionComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"default", None))
        self.videoExtensionComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u".webm", None))
        self.videoExtensionComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u".mp4", None))
        self.videoExtensionComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u".mkv", None))
        self.videoExtensionComboBox.setItemText(
            4, QCoreApplication.translate("MainWindow", u".avi", None))
        self.videoExtensionComboBox.setItemText(
            5, QCoreApplication.translate("MainWindow", u".mov", None))
        self.videoExtensionComboBox.setItemText(
            6, QCoreApplication.translate("MainWindow", u".wmv", None))

        # if QT_CONFIG(tooltip)
        self.videoExtensionComboBox.setToolTip(
            QCoreApplication.translate("MainWindow", u"Selects Default Video Downloading Extension", None))
        # endif // QT_CONFIG(tooltip)
        self.settingAudioExtensionLabel.setText(
            QCoreApplication.translate("MainWindow", u"Default Audio Extension", None))
        self.audioExtensionComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"default", None))
        self.audioExtensionComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u".m4a", None))
        self.audioExtensionComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u".wav", None))
        self.audioExtensionComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u".mp3", None))
        self.audioExtensionComboBox.setItemText(
            4, QCoreApplication.translate("MainWindow", u".aac", None))
        self.audioExtensionComboBox.setItemText(
            5, QCoreApplication.translate("MainWindow", u".pcm", None))

        # if QT_CONFIG(tooltip)
        self.audioExtensionComboBox.setToolTip(
            QCoreApplication.translate("MainWindow", u"Selects Default Audio Downloading Extension", None))
        # endif // QT_CONFIG(tooltip)
        self.settingPlaySoundLabel.setText(QCoreApplication.translate(
            "MainWindow", u"MediaPlayer Sound", None))
        # if QT_CONFIG(tooltip)
        self.playSoundBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Enables Sound From The Application", None))
        # endif // QT_CONFIG(tooltip)
        self.playSoundBtn.setText(
            QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.settingVolumeLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Default Volume", None))
        self.defaultVolumeComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"100", None))
        self.defaultVolumeComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"80", None))
        self.defaultVolumeComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"60", None))
        self.defaultVolumeComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"40", None))
        self.defaultVolumeComboBox.setItemText(
            4, QCoreApplication.translate("MainWindow", u"20", None))

        # if QT_CONFIG(tooltip)
        self.defaultVolumeComboBox.setToolTip(
            QCoreApplication.translate("MainWindow", u"Choose Default Volume For The Application's Media Player", None))
        # endif // QT_CONFIG(tooltip)
        self.settingThemeLabel.setText(
            QCoreApplication.translate("MainWindow", u"Theme", None))
        # if QT_CONFIG(tooltip)
        self.darkModeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Toggles Different Themes", None))
        # endif // QT_CONFIG(tooltip)
        self.darkModeBtn.setText(
            QCoreApplication.translate("MainWindow", u"Dark", None))
        self.notificationSoundLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Notification Sound", None))
        self.appSoundBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Enabled", None))
        self.appSoundBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Toggles App's Notification Sound", None))
        self.forceRescanLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Force Recans Files", None))
        self.forceRescanBtn.setText(
            QCoreApplication.translate("MainWindow", u"Rescan", None))
        self.forceRescanBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Rescans the Default Download Directory", None))
        self.randInitBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Enabled", None))
        self.randInitBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Toggles Initial Search Results Shown on App Starting", None))
        self.loggerLabel.setText(
            QCoreApplication.translate("MainWindow", u"Logger", None))
        self.loggerBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Disabled", None))
        self.helpMenuLabel.setText(
            QCoreApplication.translate("MainWindow", u"Help", None))
        # if QT_CONFIG(tooltip)
        self.closeHelpMenuBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close Help Menu", None))
        # endif // QT_CONFIG(tooltip)
        self.closeHelpMenuBtn.setText("")
        self.helpTextLabel.setText(QCoreApplication.translate("MainWindow",
                                                              u"Feedback: Email us at morpheusprefecttt@gmail.com. Happy downloading!",
                                                              None))
        # if QT_CONFIG(tooltip)
        self.youtubeIconBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Redirects To YouTube ", None))
        # endif // QT_CONFIG(tooltip)
        self.youtubeIconBtn.setText("")
        self.appNameLabel.setText(QCoreApplication.translate(
            "MainWindow", u"YouTube Downloader", None))
        # if QT_CONFIG(tooltip)
        self.themeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Toggle Themes", None))
        # endif // QT_CONFIG(tooltip)
        self.themeBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Toggles Notification", None))
        # endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
        self.speedIconLabel.setText("")
        self.internetSpeedLabel.setText(
            QCoreApplication.translate("MainWindow", u"0 B", None))
        # if QT_CONFIG(tooltip)
        self.networkBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Shows Internet Connectivity Status", None))
        # endif // QT_CONFIG(tooltip)
        self.networkBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.appMinBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.appMinBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.appMaxBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Toggles Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.appMaxBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.appCloseBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.appCloseBtn.setText("")
        self.searchInputText.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Enter Anything To Search...", None))
        # if QT_CONFIG(tooltip)
        self.searchBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Search On YouTube For The Provided Inputs", None))
        self.loadingIcon.setText("")
        self.loadingLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Loading...", None))
        self.initIcon.setText("")
        self.initLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Initializing...", None))
        self.downloadsMainLabel.setText(
            QCoreApplication.translate("MainWindow", u"Downloads", None))
        self.filesLabel.setText(
            QCoreApplication.translate("MainWindow", u"Files", None))
        self.sortByLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Sort By:", None))
        self.filesSortComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.filesSortComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Type", None))
        self.filesSortComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Size", None))
        self.filesSortComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"Time", None))
        self.randInitLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Random Init Search", None))
        self.randInitBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Disabled", None))

        self.playerTitleLabel.setText(
            QCoreApplication.translate("MainWindow", u"Media Player: Title of the Media", None))
        self.currentPlayingTimeLabel.setText(
            QCoreApplication.translate("MainWindow", u"--:--:--", None))
        self.mediaLengthLabel.setText(
            QCoreApplication.translate("MainWindow", u"--:--:--", None))
        # if QT_CONFIG(tooltip)
        self.fileOpenBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Selects Folder For Adding Media To Playlist", None))
        # endif // QT_CONFIG(tooltip)
        self.fileOpenBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.mediaLockBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Locks/Unlocks Media Player", None))
        # endif // QT_CONFIG(tooltip)
        self.mediaLockBtn.setText("")
        self.mediaTitleLabel.setText(QCoreApplication.translate(
            "MainWindow", u"PyPlayer: Empty Playlist!", None))
        self.seekBackwardBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.mediaPreviousBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Media Previous Button", None))
        # endif // QT_CONFIG(tooltip)
        self.mediaPreviousBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.mediaPlayBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Media Play/Pause Button", None))
        # endif // QT_CONFIG(tooltip)
        self.mediaPlayBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.mediaNextBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Media Next Button", None))
        # endif // QT_CONFIG(tooltip)
        self.mediaNextBtn.setText("")
        self.seekForwardBtn.setText("")
        self.mediaRepeatBtn.setText("")
        self.mediaShuffleBtn.setText("")
        self.playbackSpeedCombobox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"0.5x", None))
        self.playbackSpeedCombobox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"0.75x", None))
        self.playbackSpeedCombobox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"1.0x", None))
        self.playbackSpeedCombobox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"1.25x", None))
        self.playbackSpeedCombobox.setItemText(
            4, QCoreApplication.translate("MainWindow", u"1.5x", None))
        self.playbackSpeedCombobox.setItemText(
            5, QCoreApplication.translate("MainWindow", u"1.75x", None))
        self.playbackSpeedCombobox.setItemText(
            6, QCoreApplication.translate("MainWindow", u"2.0x", None))

        self.videoWidgetBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.mediaMuteBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Media Mute Button", None))
        # endif // QT_CONFIG(tooltip)
        self.mediaMuteBtn.setText("")
        self.playerOffBtn.setText("")
        self.historyStackLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Download History", None))
        self.notificationLabel.setText(QCoreApplication.translate(
            "MainWindow", u"You have been notified!", None))
        # if QT_CONFIG(tooltip)
        self.clearNotificationBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Hide Current Notification", None))
        # endif // QT_CONFIG(tooltip)
        self.clearNotificationBtn.setText("")
        self.footerLabel.setText(QCoreApplication.translate(
            "MainWindow", u"\u00a9 @chinmaykrishnroy", None))
        self.githubProfileBtn.setText("")
        self.linkedinProfileBtn.setText("")
        self.instagramProfileBtn.setText("")
        self.resizeIconLabel.setText("")
    # retranslateUi
