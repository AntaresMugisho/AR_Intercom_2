

class LineEdit:
    style_normal = """
        QLineEdit{
            border:2px solid; 
            border-radius:20px;
            font-size:18px;
            padding-left:15px;
            padding-right:15px; 
            border-color:#FFFFFF; 
            background-color:#FFFFFF;}
    
        QLineEdit:hover,  QLineEdit:focus{
            border-color: rgba(57, 146, 240, 180);}
        
        """

    style_error = """
        QLineEdit{border:2px solid; 
            border-radius:20px;
            font-size:18px;
            padding-left:15px;
            padding-right:15px; 
            border-color:#99FF0000; 
            background-color:#FFFFFF;}
        
        QLineEdit:hover{
            border-color:#C5C5C5;}   
            
        QLineEdit:focus{
            border-color: rgba(57, 146, 240, 180);} 
            
        """

class ComboBox:
    style_normal = """
        QComboBox{
            border:2px solid #FFF; 
            border-radius:20px;
            font-size:18px;
            padding-left:15px;
            padding-right:15px; 
            background-color:#FFFFFF;
            color:#80000000;}

        QComboBox::drop-down{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left-width: 1px;
            border-left-style: solid;
            border-left-color: rgba(57, 146, 240, 180);
            border-top-right-radius: 2px;
            border-bottom-right-radius: 3px;
            background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);
            background-position: center;
            background-repeat: no-reperat;}
        
        QComboBox:hover, QComboBox:focus{
            border-color: rgba(57, 146, 240, 180);}
        
        QComboBox QAbstractItemView {
            color:#000;
            background-color:#FFF;
            padding: 10px;
            selection-color:#3385CC;
            selection-background-color:#10000000;}
        
        """

    style_error = """
        QComboBox{
            border:2px solid #99FF0000; 
            border-radius:20px;
            font-size:18px;
            padding-left:15px;
            padding-right:15px; 
            background-color:#FFFFFF;
            color:#80000000;}

        QComboBox::drop-down{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left-width: 1px;
            border-left-style: solid;
            border-left-color: #99FF0000;
            border-top-right-radius: 2px;
            border-bottom-right-radius: 3px;
            background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);
            background-position: center;
            background-repeat: no-reperat;}

        QComboBox QAbstractItemView {
            color:#000;
            background-color:#FFF;
            padding: 10px;
            selection-color:#3385CC;
            selection-background-color:#10000000;}

        QComboBox:hover{
            border-color:#C5C5C5;}
        
        QComboBox::drop-down{
            border-left-width:1px;
            border-left-color:#C5C5C5;}
    
        QComboBox:focus{
            border-color:rgba(57, 146, 240, 180);}
        
        QComboBox::drop-down:focus{
            border-left-color:rgba(57, 146, 240, 180);}
        
        """

class Features:
    style_active = """
        QPushButton{
            background-color:#3385CC;
            border-radius:7px;}"""

    style_inactive = """
        QPushButton{
            background-color:#EAEAEA;
            border-radius:7px;}

        QPushButton:hover{
            background-color:#3385CC;}"""

    prev = """
        QPushButton{
            border:none;
            background:none;}
    
        QPushButton:hover{
            border-radius:15px;
            background-color:#0055FF;
            background-image: url(:/cils/cils/cil-chevron-circle-left-alt.png);
            background-position:center;
            background-repeat:no-repeat;}"""

    next = """
            QPushButton{
                border:none;
                background:none;}

            QPushButton:hover{
                border-radius:15px;
                background-color:#0055FF;
                background-image: url(:/cils/cils/cil-chevron-circle-right-alt.png);
                background-position:center;
                background-repeat:no-repeat;}"""

class Clients:
    frame_normal = """
        QFrame{
            border-top:1px solid #FFF;
            border-bottom:1px solid #FFF;}
            
        QFrame:hover{
            border-top:1px solid #FFAA00;
            border-bottom:1px solid #FFAA00;}
        
        """

    frame_unread_msg = """
        QFrame{
            background-color:#FFAA00;
            border-top:1px solid #FFF;
            border-bottom:1px solid #FFF;}
            
        QFrame:hover{
            border-top:1px solid #FFF;
            border-bottom:1px solid #FFF}"""

class ScrollBar:
    orange_style = """
        QScrollBar:vertical{
            border: none;
            background: rgb(52, 59, 72);
            width: 10px; 
            margin: 18px 0 18px 0; 
            border-radius: 0px;}

        QScrollBar::handle:vertical{
            background: #FFAA00; 
            min-height: 25px; 
            border-radius: 5px;}

        QScrollBar::add-line:vertical{
            border: none; 
            background: #00003B;
            height: 17px;
            border-bottom-left-radius: 5px; 
            border-bottom-right-radius: 5px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;}

        QScrollBar::sub-line:vertical{
            border: none; 
            background: #00003B; 
            height: 17px;
            border-top-left-radius: 5px; 
            border-top-right-radius: 5px;
            subcontrol-position: top;
            subcontrol-origin: margin;}

        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
            background: none;}

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: #2800003B;}
        
        """

    blue_style = """
        QScrollArea{
            border:1px solid; 
            border-color: #FFAA00; 
            background-color: rgb(255, 255, 255);
            border-top-right-radius:5px; 
            border-radius:5px;
            margin-left:10px;}
       
        /* VERTICAL SCROLL */  
            
        QScrollBar:vertical{
            border: none;
            background: #CCDDFF;
            width: 10px; 
            margin: 18px 0 18px 0; 
            border-radius: 0px;}

        QScrollBar::handle:vertical{
            background: #3385CC;
            min-height: 25px; 
            border-radius: 5px;}

        QScrollBar::add-line:vertical{
            border: none; 
            background: #00003B;
            height: 17px;
            border-bottom-left-radius: 5px; 
            border-bottom-right-radius: 5px;
            subcontrol-position: bottom; 
            subcontrol-origin: margin;}

        QScrollBar::sub-line:vertical{
            border: none; 
            background: #00003B; 
            height: 17px;
            border-top-left-radius: 5px; 
            border-top-right-radius: 5px;
            subcontrol-position: top;
            subcontrol-origin: margin;}

        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
            background: none;}

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;}
                
        /* HORIZONTAL SCROLL */
        
        QScrollBar:horizontal{
            border: none;background: #CCDDFF;
            height: 10px; margin: 0 18px 0 18px; 
            border-radius: 0px;}

        QScrollBar::handle:horizontal{
            background: #3385CC; 
            min-width: 25px; 
            border-radius: 5px;}

        QScrollBar::add-line:horizontal{
            border: none; 
            background: #00003B;
            width: 17px;"
            border-bottom-left-radius: 5px; 
            border-top-left-radius: 5px;
            subcontrol-position: left; 
            subcontrol-origin: margin;}

        QScrollBar::sub-line:horizontal{
            border: none; 
            background: #00003B;
            width: 17px;
            border-top-right-radius: 5px; 
            border-bottom-right-radius: 5px;
            subcontrol-position: right;
            subcontrol-origin: margin;}

        QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{
            background: none;}

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{
            background: none;}

        """

class MessageStatus:
    style_sent = """
        QPushButton{
            image:url(:/cils/cils/cil-check-circle-green.png);
            border:none; 
            background:none;}
        """

    style_not_sent = """
        QPushButton{
            image:url(:/cils/cils/cil-reload-red.png);
            border:none; 
            background:none;} 
        """

class MediaButton:
    style_more = """
        QPushButton{
            image: url(:/icons/icons/More.png); 
            border:none;
            border-radius:20px;} 
            
        QPushButton:hover{
            border:1px solid #3385CC;}"
        """

    style_less = """
        QPushButton{
            image: url(:/icons/icons/Less.png); 
            border:none;
            border-radius:20px;} 
        QPushButton:hover{
            border:1px solid #3385CC;}
        """

class SendButton:
    style_send = """
        QPushButton{
            image: url(:/icons/icons/send.png); 
            border:none;
            border-radius:20px;}
        
        QPushButton:hover{
            border:1px solid #3385CC;})
        """

    style_record = """
        QPushButton{
            image: url(:/icons/icons/record.png); 
            border-radius:20px;}

        QPushButton:hover{
            border:1px solid #3385CC;})
            
        """

class Player:
    play = """
        QPushButton{
            background-image: url(:/cils/cils/cil-media-play.png);
            background-repeat: no-repeat;
            background-position:center;
            border-radius:6px;
            border:none;}

        QPushButton::hover{
               border:1px inset rgba(255, 255, 255, 0.6);}
        
        QPushButton::pressed{
               border:2px inset rgba(255, 255, 255, 1);}   
        """

    pause = """
        QPushButton{
            background-image: url(:/cils/cils/cil-media-pause.png);
            background-repeat: no-repeat;
            background-position:center;
            border-radius:6px;
            border:none;}
            
        QPushButton::hover{
               border:1px inset rgba(255, 255, 255, 0.6);}
        
        QPushButton::pressed{
               border:2px inset rgba(255, 255, 255, 1);} 
        """

class Slider:

    slider = """
        QSlider{
            background:none;}
    
        QSlider::groove:horizontal{ 
            height:4px;
            border:none;}
        
        QSlider::handle:horizontal{
            height:12px;
            width:12px;
            border-radius:6px;
            margin:-4px 0px -4px 0px;
            background-color: rgba(0, 121, 215, 255);}
            
        QSlider::handle:hover{
            background-color: rgba(0, 52, 93, 255);}
        
        QSlider::handle:pressed{
            background-color: rgba(0, 121, 215, 255);}
        
        QSlider::add-page:horizontal{
            background-color:#55FFFFFF;}
        
        QSlider::sub-page:horizontal{
            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
            stop:0 rgba(0, 52, 93, 255), stop:1 rgba(0, 121, 215, 255));}
        """


