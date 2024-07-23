* {
	border: none;
    padding: 0px;
    margin: 0px;
    background-color: transparent;
    font-family: "Segoe UI";
    font-size: 16px;
}

/*216869*/

QPushButton {
    color: #F1FAEE;  /*Off White Palette Color*/
}

QLabel {
    color: #F1FAEE;  /*Off White Palette Color*/
}

QScrollArea {
    border: none;
}

QScrollBar:vertical {
    width: 4px;
    margin: 10px 0px 10px 0px;
}

QScrollBar:horizontal {
    height: 4px;
    margin: 0px 40px 0px 40px;
}

QScrollBar:vertical, QScrollBar:horizontal {
    background: #F1FAEE;
    border-radius: 2px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #424242;
    border-radius: 2px;
    min-height: 20px;
    min-width: 20px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: #fb4c24;
    border-radius: 2px;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: transparent;
}


/*/////////////////////////////////////HEADER//////////////////////////////////////////*/

#headerContainer {
	background: #030301;
}

#appNameLabel{
	color: #F1FAEE; /*Light Blue Palette Color*/
}

#youtubeIconBtn {
	background-color: #ff0000;
	margin-left: 36px;
	margin-top: 5px;
	border-radius: 4px
}

#appCloseBtn:hover {
    background-color: #ff0000; 
}

#appCloseBtn:pressed {
    background-color: #000000;
}

#networkBtn, #notificationBtn, #themeBtn {
	border: 1px dotted transparent;
	border-radius: 15px;
}

#appMinBtn:hover, #appMaxBtn:hover, #networkBtn:hover, #notificationBtn:hover, #themeBtn:hover {
    background-color: #16161f;
}

#networkBtn:pressed, #notificationBtn:pressed, #themeBtn:pressed{
    background-color: #fb4c24;
}

#appMinBtn:pressed, #appMaxBtn:pressed{
    background-color: #222222;
}

#internetSpeedLabel {
	font-size: 10px;
}

#youtubeIconBtn:hover {
    background-color: #999999;
}

#youtubeIconBtn:pressed {
    background-color: #000000;
}

#appNameLabel {
    font-size: 20px;
    font-weight: bold;
    color: #F1FAEE;
    text-align: center;
}

/*/////////////////////////////////////END-HEADER//////////////////////////////////////*/

/*///////////////////////////////////////LEFT-MENU//////////////////////////////////////*/

#centralwidget {
    background-color: #181C1F; /*Left Menu Black Color*/
}

#leftMenuContainer {
    background-color: #030301;  /*Left Menu Black Color*/
}

#leftMenuSubContainer QPushButton {
    text-align: left;
	margin: 4px 4px;
    padding: 8px 8px;
    padding-right: 20px;
}

#mainStackBtnsFrame  QPushButton{
	padding-left: 12px;
}

#menuFrame QPushButton:hover {
    border-radius: 6px;
}

#mainStackBtnsFrame QPushButton:hover {
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
}

#leftMenuSubContainer QPushButton:hover {
    background-color: #16161f;  /*Left Menu Hover Grey Color*/
    border-style: solid;
    border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
}

#leftMenuSubContainer QPushButton:pressed {
    color: #000000;
    background-color: #fb4c24; /*Left Menu Click Lighter Grey Color*/
}

#settingHelpBtnFrame  QPushButton{
	padding-left: 12px;
}

/*////////////////////////////////////LEFT-MENU-END////////////////////////////////////////*/

/*//////////////////////////////////////CENTER-MENU////////////////////////////////////////*/

#centerMenuSubContainer {
    background-color: #fb4c24;  /*Palette Dark Blue Color*/
}

#settingMenu {
    background-color: #111111;  /*Left Menu Black Color*/
    border-radius: 0px;
}

#settingMenu QLabel {
	font-size: 20px;
	font-weight: bold;
	padding-bottom: 4px;
}

#settingPageBtnsWidget QLabel {
	font-size: 16px;
	margin-top: 15px;
	margin-bottom: 6px;
}

#settingPageBtnsWidget QPushButton {
	color: #A8DADC;
	font-size: 14px;
	background: #0a0a06;
	border-radius: 4px;
	padding: 6px 8px;
	text-align: left;
}

#settingPageBtnsWidget QPushButton:hover {
	background: #16161f;
}

#settingPageBtnsWidget QComboBox:hover {
	background: #16161f;
}

#settingPageBtnsWidget QPushButton:pressed {
	background: #444444;
}

#settingPageBtnsWidget QComboBox {
	color: #A8DADC;
	font-size: 14px;
	background: #0a0a06;
	border-radius: 4px;
	text-align: left;
	padding: 6px 8px;
	padding-left: 8px;
	border: none;
}

#settingPageBtnsWidget QComboBox::drop-down {
    selection-background-color: #3240ee;
    border-radius: 8px;
}

#settingPageBtnsWidget QComboBox::down-arrow {
  	image: transparent;
    border-radius: 8px;
}

#settingPageBtnsWidget QComboBox QAbstractItemView {
	color: #F1FAEE;
    selection-background-color: #3240ee;
}

#settingPageBtnsWidget QComboBox:pressed {
	background: #444444;
}

#helpMenu {
    background-color: #111111;  /*Left Menu Black Color*/
    border-radius: 0px;
}

#helpMenu QLabel {
	font-size: 20px;
	font-weight: bold;
	padding-bottom: 4px;
}

#helpTextLabel {
	font-size: 14px;
	padding: 4px 8px;
	color: black;
}

#closeHelpMenuBtn,  #closeSettingMenuBtn {
	border: 2px solid transparent;
    border-radius: 14px;
}

#closeSettingMenuBtn:hover, #closeHelpMenuBtn:hover {
    background-color: #333333;
}

#closeSettingMenuBtn:pressed, #closeHelpMenuBtn:pressed {
    background-color: #000000;
}

/*////////////////////////////////////CENTER-MENU-END/////////////////////////////////////*/

/*///////////////////////////////////////MAIN-STACK//////////////////////////////////////////*/

#mainAppBody {
	background-color: #030301;
}

#mainAppStack {
	background-color: #030301;
}

/*//////////////////////////////////////INIT-STACK////////////////////////////////////////*/

#initStack QLabel {
	font-size: 28px;
}

#initIcon {
    background-image: url(:/gif/catDark.gif);
}

/*//////////////////////////////////////END INIT-STACK////////////////////////////////////////*/


/*//////////////////////////////////////LOADING-STACK////////////////////////////////////////*/

#loadingStack QLabel {
	font-size: 28px;
}

#loadingIcon {
    background-image: url(:/gif/catDark.gif);
}

/*//////////////////////////////////////END LOADING-STACK////////////////////////////////////////*/


/*//////////////////////////////////////SEARCH-STACK////////////////////////////////////////*/

#searchStack {
	background: #111111; /*Deep Ocean Blue Body Background Color*/
	border-radius: 10px;
}

#searchBtn {
	background-color: #ff0000;
	padding: 4px 32px;
    border: 2px solid #ff0000;
	border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
}

#searchBtn:hover {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #380036, stop:1 #0CBABA);  /*YouTube Search Button Red Color*/
    border: 2px solid #111111;
}

#searchBtn:pressed {
    background-color: #EFA00B;  /*Palette Brown Color*/
    border: 2px solid #EFA00B;  /*YouTube Search Button Red Color*/
}

#searchInputText {
	background: #F1FAEE; /*Off White Palette Color*/
	padding-top: 6px;
	padding-bottom: 3px;/****************************/
	padding-left: 12px;
	padding-left: 12px;
	border: 1px solid #F1FAEE; /*Off White Palette Color*/
	border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
}

/*/////////////////////////////////VIDEO-CONTAINER/////////////////////////////////////*/

#videoContainer {
	background: #374a67; /*Video Container Grey Color*/
	border-radius: 8px;
}

#videoThumbnailFrame {
	background-color: #111111;
	border-radius: 8px;
}

#viewsLabel {
	font-size: 12px;
	margin-left: 46px;
	font-family: "Roboto", "Arial", "sans-serif";
}

#videoTitleLabel {
	font-size: 14px;
	margin-left: 14px;
	font-family: "Roboto", "Arial", "sans-serif";
}

#videoDurationLabel {
	font-size: 12px;
	font-family: "Roboto", "Arial", "sans-serif";
	padding: 2px 4px;
	background : rgba(0,0,0, 0.4);
	border-radius: 4px;
	margin-top: 4px;
	
}

#channelNameLabel {
	font-size: 12px;
	margin-top: 10px;
	margin-left: 46px;
	font-family: "Roboto", "Arial", "sans-serif";
}

#downloadPageRedirectBtn {
	font-size: 16px;
	border: 1px solid transparent;
	border-radius: 8px;
	margin-bottom: 4px;
	margin-left:4px;
}

#downloadPageRedirectBtn:hover {
    background-color: #16161f; 
}

#downloadPageRedirectBtn:pressed {
    background-color: #fb4c24;
}

#streamBtn {
	font-size: 16px;
	border: 1px solid transparent;
	border-radius: 8px;
	margin-bottom: 4px;
	margin-right:4px;
}

#streamBtn:hover {
    background-color: #16161f; 
}

#streamBtn:pressed {
    background-color: #fb4c24;
}

/*////////////////////////////////VIDEO-CONTAINER-END//////////////////////////////////*/

/*//////////////////////////////////SEARCH-STACK-END////////////////////////////////////*/

/*///////////////////////////////////DOWNLOAD-STACK////////////////////////////////////*/

#downloadStack QScrollArea {
    border: none;
}

#downloadStack {
	background: #111111;
	border-radius:10px;
}

#downloadsMainLabel{
	font-size: 28px;
	padding-left: 8px;
	padding-top: 4px;
}

#downloadItemFrame {
	background: #030301;
	border-radius: 8px;
}

#downloadItemFrame QSlider {
	background: transparent;
    height: 5px;
}

#downloadMediaTitleLabel{
	padding: 0px 8px;
}

#downloadItemFrame QSlider::groove:horizontal {
    border: none;
    height: 5px;
    background: #151515;
    border-radius: 2px;
}

#downloadItemFrame QSlider::handle:horizontal {
    width: 5px;
    background: #fb4c24;
    border-radius: 2px;
}

#downloadItemFrame QSlider::sub-page:horizontal {
    background: #404040;
	margin-left: 2px;
	width: 5px;
    border-radius: 2px;
}

#downloadsMainLabel QLabel {
	font-size: 28px;
	padding-left: 8px;
	padding-top: 4px;
}

#qualitySelectWidget QRadioButton {
	font-size: 11px;
	color: #F1FAEE;  /*Media Quality Radio Button Blue Color*/
}

#qualitySelectWidget QPushButton  {
	font-size: 16px;
	padding: 4px 6px;
	background: #fb4c24;  /*Reddish Download Button Color*/
	border-radius: 8px;
}

#qualitySelectWidget QPushButton:hover {
	background: #222222;
}

#qualitySelectWidget QPushButton:pressed {
	background: #475B63;
}

#downloadProgressFrame QLabel {
	font-size: 12px;
	padding: 0px 8px;
}

#downloadProgressFrame QPushButton  {
	font-size: 14px;
	padding: 4px 6px;
	background: #fb4c24;
	border-radius: 8px;
	padding: 2px 6px;
}

#downloadProgressFrame QPushButton:hover {
	font-size: 14px;
	background: #222222;
}

#downloadProgressFrame QPushButton:pressed {
	font-size: 14px;
	background: #333333;
}

#homeRedirectBtn:pressed {
	border-radius: 4px;
    background-color: #222229;
}

/*////////////////////////////////DOWNLOAD-STACK-END/////////////////////////////////*/

/*//////////////////////////////////////FILES-STACK/////////////////////////////////////////*/
#filesStack{
	background: #111111;
	border-radius: 10px;
}

#filesLabel {
	font-size: 28px;
	padding-left: 8px;
	padding-top: 4px;
}

#filesUtilityFrame QLabel {
    color: black;
	padding:2px 8px;
	padding-bottom:2px;
	margin-bottom:4px;
    color: #FFEEDD;
	font-family: "Segoe UI";
	font-size: 16px; 
}

#filesUtilityFrame QPushButton {
	border: 1px dotted transparent;
	border-radius: 15px;
}

#filesUtilityFrame QPushButton:hover {
    background-color: #16161f;
}

#filesUtilityFrame QPushButton:pressed{
    background-color: #fb4c24;
}


#filesUtilityFrame QComboBox {
	background-color:#1f1f1f; 
	text-align: left;
	width: 36px;
	padding: 2px 4px;
    color: #FFEEDD;
	font-family: "Segoe UI";
	font-size: 14px; 
    border-radius: 6px;
}

#filesUtilityFrame QComboBox:hover {
	background-color:#33383E; 
	border-style: solid; 
	border-radius: 6px;
}

#filesUtilityFrame QComboBox:pressed {
	background-color: #232324; 
	border-style: solid; 
	border-radius: 6px;
}

#filesUtilityFrame QComboBox QAbstractItemView {
    color: white;
    background-color: #000000;
    selection-background-color: #fb4c24; 
	border-radius: 2px;
}


#filesUtilityFrame QComboBox:focus {
}

#filesUtilityFrame QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}

#files {
	border-radius: 8px;
	background: #030301;
}

#fileTitleFrame QLabel {
	font-size:18px;
    margin: 0px 4px;
}

#fileInfoFrame QLabel {
	font-size:16px;
	margin: 0px 6px;
}

#fileTypeFrame QLabel {
	font-size:14px;
	margin: 8px 4px;
}

#files QPushButton:hover {
    background-color: #555555; 
	border-bottom-left-radius: 8px;
}

#files QPushButton:pressed {
    background-color: #0b6b43; 
	border-bottom-left-radius: 8px;
}

#endOfFilesBtn:pressed {
	border-radius: 4px;
    background-color: #222229;
}

/*////////////////////////////////////MEDIA-PLAYER///////////////////////////////////////*/

#mediaPlayer{
	background: #030301;
	border-radius: 10px;
}

#mediaPlayerFrame QFrame {
    background-color: #fb4c24; /*0b6b43*/
	font-family: "Helvetica", sans-serif;
}

#mediaProgressFrame QLabel {
background: transparent;
color: #FFEEDD;
font-family: "Helvetica", sans-serif;
font-size: 11px;
}

#mediaProgressFrame QSlider {
    background: transparent;
    height: 6px;
}

#mediaProgressFrame QSlider::groove:horizontal {
    border: none;
    height: 6px;
    background: #000000;
    border-radius: 3px;
}

#mediaProgressFrame QSlider::handle:horizontal {
    width: 6px;
    background: #FFEEDD;
    border-radius: 3px;
}

#mediaProgressFrame QSlider::sub-page:horizontal {
    background: #A6A6A6;
	margin-left: 0px;
	width: 6px;
    border-radius: 3px;
}

#mediaButtonsFrame QFrame {
    background-color: #0F111A; 
}

#mediaButtonsFrame QLabel {
background: transparent;
color: #FFEEDD;
margin-left: 3px;
margin-right: 3px;
font-family: "Segoe UI";
font-size: 12px; 
}

#mediaButtonsFrame QPushButton { 
	background: transparent;
}

#mediaButtonsFrame QPushButton:hover {
	background-color:#33383E; 
	border-style: solid; 
	border-radius: 2px; 
}

#mediaButtonsFrame QPushButton:pressed {
	background-color: #4455FF; 
	border-style: solid; 
	border-radius: 2px; 
}

#mediaButtonsFrame QComboBox {
    color: black;
	padding-left: 4px;
    color: #FFEEDD;
	font-family: "Segoe UI";
	font-size: 10px; 
}

#mediaButtonsFrame QComboBox:hover {
	background-color:#33383E; 
	border-style: solid; 
	border-radius: 2px; 
}

#mediaButtonsFrame QComboBox:pressed {
	background-color: #232324; 
	border-style: solid; 
	border-radius: 2px; 
}

#mediaButtonsFrame QComboBox QAbstractItemView {
    color: white;
    background-color: #000000;
    selection-background-color: #fb4c24; 
    border: none;
}


#mediaButtonsFrame QComboBox:focus {
}

#mediaButtonsFrame QComboBox::drop-down:button
{
    border: none;
    padding: 0;
    width: 0;
}

#mediaButtonsFrame QSlider {
    background: transparent;
    height: 5px;
	padding-left:2px;
	padding-right:2px;
}

#mediaButtonsFrame QSlider::groove:horizontal {
    border: none;
    height: 5px;
    background: #000000;
    border-radius: 2px;
}

#mediaButtonsFrame QSlider::handle:horizontal {
    width: 5px;
    background: #FFEEDD;
    border-radius: 2px;
}

#mediaButtonsFrame QSlider::sub-page:horizontal {
    background: #38B6FF;
	margin-left: 0px;
	width: 5px;
    border-radius: 2px;
}

#videoPlaybackFrame QLabel {
	margin: 2px 8px;
}

/*///////////////////////////////////MEDIA-PLAYER-END///////////////////////////////////*/

/*///////////////////////////////////FILES-STACK-END//////////////////////////////////////*/

/*////////////////////////////////////HISROY-STACK////////////////////////////////////////*/

#historyStack {
	background: #111111;
	border-radius: 10px;
}

#historyStackLabel{
	font-size: 28px;
	padding-left: 8px;
	padding-top: 4px;
}

#historyItem {
	background: #030301;
	border-radius: 8px;
}

#historyInfoFrame QLabel{
	font-size:14px;
	margin: 2px 4px;
}

#titleHistoryItemFrame QLabel{
	font-size:20px;
	margin: 2px 4px;
}

#noMoreHistoryBtn {
	background: transparent;
}

#noMoreHistoryBtn:pressed {
	border-radius: 4px;
    background-color: #222229;
}

/*////////////////////////////////HISROY-STACK-END////////////////////////////////////*/

/*/////////////////////////////////MAIN-STACK-END//////////////////////////////////////*/

/*//////////////////////////////////NOTIFICATION///////////////////////////////////////*/

#notificationWiget {
	background: #030301;
}

#notificationFrame {
	background: #030301;
	margin: 4px;
	border: 2px solid #222222;
	border-radius: 8px;
}

#notificationLabel {
	font-size: 18px;
	padding: 6px 8px;
} 

#clearNotificationBtn {
	margin-right: 8px;
	border-radius: 4px;
}

#clearNotificationBtn:hover {
    background-color: #2d2d2d;
}

#clearNotificationBtn:pressed {
    background-color: #fb4c24;
}

/*////////////////////////////////NOTIFICATION-END////////////////////////////////////*/


/*///////////////////////////////////////FOOTER///////////////////////////////////////////*/

#footerFrame {
	background: #030301;
}

#footerLabel {
	font-size: 12px;
	margin-left: 4px;
	margin-right: 4px;
	margin-bottom: 5px;
} 

#footer QPushButton:hover {
	border-radius: 4px;
    background-color: #fb4c24;
}

#footer QPushButton:pressed {
	border-radius: 4px;
    background-color: #555555;
}

/*////////////////////////////////////FOOTER-END////////////////////////////////////////*/