
Country = ['台灣']
Background = [['老爸是大老闆，上下學專車接送，家裡有3個傭人，超爽', 
            '沒什麼好說，總之是個還過得去的一般家庭', 
            '不知道下一餐在哪裡，多災多難的貧困家庭']
]
Event = [['光陰似箭，歲月如梭，身為富二代的你成年了，也到了決定人生方向的時候了\n\n自己決定吧',
        '時間過得真快，一眨眼就成年了，該替自己的未來打算了\n\n決定吧',
        '雖然以前常常餓肚子，但還是順利長大了，沒爸可靠的你下一步要怎走呢？\n想清楚吧'],
]
Ending = [[['哇，人生好順利喔', 
        '剛開始真的很痛苦，以前的高級消費娛樂都不能做了，但回想起自己過去的人生，其實也算渾渾噩噩，於是開始利用時間充實自己，認識許多業界成功的人士，參與了許多課程，最後靠著3年的100萬積蓄，再加上老爸給的4900萬，買下台北精華區的人生第一棟房子\n『有夢最美，逐夢踏實』', 
        '『不想活在父親的陰影下』，八年前選擇不繼承家業，差點被老爸斷絕關係，如今自己當了老闆開了公司，也算是小有成就\n......\n想不到，上個月老爸硬是砸錢把我的公司全部股權買下，要回去接班了＝＝....'], 
        ['領著還行的薪水過著還行的日子，也還行拉', 
        '『啃老就要慢慢輕輕的啃才能長久』by 國動\n豪爽喔\n每天打game尻尻，時間一下就消磨掉了，吃家裡剩的，當家裡的廚餘桶，偶爾幫忙跑腿（找的錢還可以當零用錢），阿...斯...\n再...再讓我啃兩年...', 
        '噫！好了！我中了！\n考了第三年終於考上囉，鐵飯碗get！，想當初被質疑在家當米蟲，鄰居也常常閒言閒語，我就說一句\n讀書人的事，稱得上米蟲嗎？\n'], 
        ['每天上班下班，勉強餬口，好想要有個有錢的老爸', 
        '社會在走，行情要有\n幹，上次那個阿吃嘴小孩還沒來跟我道歉，是當拎被塑膠？我也是笑笑而已拉',
        '『人生可以黑白，但千萬不能迷彩』，幹你娘如果回到四年前我一定把當初要簽下去的我鼻樑打斷，這四年賠了自由、賠了光陰、賠了身體、賠了腦袋\n哀，寧做乞兒不做狗兒，早知如此去當個保全也好']]]

######################################################################
gender = ['male', 'female']

Life = {'台灣': {'老爸是大老闆，上下學專車接送，家裡有3個傭人，超爽': {'inherit', 'work', 'lazy', 'create'}, 
                  '沒什麼好說，總之是個還過得去的一般家庭': {'work', 'lazy', 'exam'}, 
                  '不知道下一餐在哪裡，多災多難的貧困家庭': {'work', 'exam', 'bad'}
                  },
#        'China': {'rich': {'inherit', 'lazy', 'work'},
#                 'normal': {'work', ''},
#                 'poor':
#                 }
    
       }
event = { 0:{ 0:{'光陰似箭，歲月如梭，身為富二代的你成年了，也到了決定人生方向的時候了\n\n自己決定吧，輸入：\n1：繼承家業\n2：出去工作\n3：在家耍廢\n4：創業' }, 
              1:{'時間過得真快，一眨眼就成年了，該替自己的未來打算了\n\n決定吧，輸入：\n1：找工作\n2：啃老\n3：考公職'}, 
              2:{'雖然以前常常餓肚子，但還是順利長大了，沒爸可靠的你下一步要怎走呢？\n\n想清楚吧，輸入：\n1：找工作\n2：跳陣頭'}
            }     
        }
ending = { 0:{ 0:{0:'000ending', 1:'001ending', 2:'002eding', 3:'003ending'},
               1:{0:'010ending', 1:'011ending', 2:'012ending'},
               2:{0:'020ending', 1:'021ending', 2:'022ending'}
             }
         }
