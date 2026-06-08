// package game;//包名，包名出错会报错
 
import java.awt.Color;//颜色
import java.awt.Font;//后面设置游戏界面绘制文字字体用的
import java.awt.Graphics;//绘制游戏界面用的
import java.awt.event.KeyEvent;//按键事件
import java.awt.event.KeyListener;//键盘监听，贪吃蛇项目需要监听玩家按下的方向键 
import javax.swing.JFrame;//窗口控件，窗口里可以放置组件
import javax.swing.JPanel;//组件，用于充当绘制游戏界面的画板
import java.util.Random;//随机数
import java.util.Timer;//定时用的
import java.util.TimerTask;//定时任务类
 
public class SnakeGame extends JPanel implements KeyListener {// 用java语言翻译成汉语就是:Demo类继承了JPanel并实现了KeyListener接口
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;// 不知道干啥的反正没加的时候编辑器就提醒加，加不加却都能运行
 
	// 以下都是全局变量与局部方法内定义的变量不同，全局变量可以在类中的任意方法中被调用，但局部变量不可以
 
	public int snakeX[] = new int[100];// 新建一个数组，用于存储蛇的每一节身体在x轴上的坐标，最多100个
 
	public int snakeY[] = new int[100];// y轴坐标，同上
 
	public int length;// 蛇有长度，用一个整数变量存储这个长度，后续蛇吃到食物这个长度会增加
 
	public String direction;// 蛇走的时候有方向，所以用一个全局变量储存
 
	public int food[] = new int[2];// 食物只有一个，所以要记录食物的坐标只需要两个整数变量,干脆一个长度为2的数组（food[0]是x坐标，food[1]是y坐标）
 
	public boolean isStart;// 是否开始游戏，按空格键开始
 
	public boolean isFail;// 你输了吗，我怎么可能会输呢，是游戏bug了
 
	public int score;// 游戏得分，现在给它赋值多少，你就能以多少分起步了，作弊模式，开启
 
	Random r = new Random();//食物的出现是随机的所以需要生成随机数，Random里有一个在给定范围内生成整数的方法，调用方法：对象.nextInt();前提是要实例化Random类为对象
 
	// 下面的Demo方法和类名重合，并且不符合构成方法头必要的三个条件(1.访问权限,例如public公开的或者private私有的 2.返回值类型例如String，表示返回的值是字符串形的，void表示没有返回值 3.方法名)
	public SnakeGame() {// 所以这不是普通的函数或方法，而是构造方法，在实例化这个类（new
					// 类名()）的时候会自动调用这个函数，有时候用这个方法代替“初始化"方法是真方便，但这次好像不能，所以需要额外再写一个
		this.setBackground(Color.white);// java语：设置游戏背景为白色，默认灰色
		this.setFocusable(true);// java语：让游戏界面成为焦点，焦点：当你的桌面上有很多界面的时候，比如说记事本和java编辑器，焦点在编辑器上的时候可以正常输入，但是此时打开记事本，焦点就会转移，把字打在记事本上，再点击一次编辑器，编辑器界面就能获得焦点，再次编辑
		this.addKeyListener(this);// 给游戏界面绑定一个键盘输入监听器，第一个this表示游戏界面，第二个表示监听器，详情请百度搜索java 继承和addKeyListener
		init();
	}
 
	public void init() {// 初始化方法，定义一个蛇，包括头长度为3，头和身体连起来占据三个相邻坐标，同时蛇的方向向右
		length = 3;
 
		snakeX[0] = 40;// 头（第一节）x坐标
		snakeY[0] = 0;// y
 
		snakeX[1] = 20;// 第二节
		snakeY[1] = 0;
 
		snakeX[2] = 0;// 三
		snakeY[2] = 0;
 
		direction = "R";// Right的缩写
		
		score = 0;//初始化后分数清零
		
		isStart = false;//先将游戏定义为未开始状态，后面加入一个按空格开始游戏的操作
		
		isFail = false;//没死之前就是没失败，对就这样定义
		
		refreshFood();//这个函数就一个刷新食物的作用
	}
 
	@Override // 重写标志 www.bai.com 关键词：@Override
	public void paint(Graphics g) {// JPanel类里的构造函数，好像和Graphics有点关系，什么关系呢，不懂。。。
		super.paint(g);// 调用父辈的paint方法 www.bai.com 关键词：重写，继承,这里的作用好像是调用这个能清空画板
		g.setColor(Color.black);// 设置画笔颜色为绿色，为什么是绿色呢，问就是不知道
		g.setFont(new Font("幼圆",Font.BOLD,20));//设置字体，后面会有直接在游戏界面显示文字的代码
		g.drawString("Score:"+score, 520, 20);//时刻显示玩家的得分情况
		if(isFail) {
			g.setFont(new Font("幼圆",Font.BOLD,30));//准备偷笑
			g.drawString("你把自己的脑子给吃了", 50, 100);//哈哈
		}
		if(!isStart) {//java语：如果游戏是未开始状态，为什么没开始呢，三种情况，一是刚打开游戏，二是结束游戏，三是pause暂停
			g.setFont(new Font("幼圆",Font.BOLD,30));//字号调大点，准备画大大的文字
			if(isFail) {//java语：如果失败了
				g.drawString("按下空格键重新开始游戏", 20, 220);//就画个“再战一轮”
			}else {//否则呢，就是说如果没有失败的话
				g.drawString("按下空格键开始游戏", 80, 220);//就表示你需要继续游戏
			}
		}
		g.fillRect(food[0], food[1], 20, 20);
		for (int i = 0; i < length; i++) {// 0~整数length,但不包括length,意为循环length次
			g.fillRect(snakeX[i], snakeY[i], 20, 20);// 画矩形，i=[0~3)所以是遍历蛇的每一节，然后画
		}
	}
 
	public static void main(String[] args) {// 主方法，没有主方法你试试
		JFrame jf = new JFrame("Snake");// 实例化JFrame，相当于新建一个窗口，()里的字符串是窗口的title，不知道title是什么意思下载有道词典去
		jf.setBounds(500, 300, 640, 480);// 设置窗口范围，四个参数依次是（离屏幕左边有多远，离上面有多远，窗口多宽，多高）
		jf.setResizable(false);// java语：可以被用户拉伸或者压缩窗口吗？不可以！
		SnakeGame d = new SnakeGame();//
		jf.add(d);// 画板固定到窗口里 画板（游戏界面）
		jf.setVisible(true);// java语：要显示窗口吗。显示，不然不让你看见
		d.doLoop();
	}
	//接下来是刷新食物的方法，食物呢要随机，而且，不能刷在蛇身上
	public void refreshFood() {
		boolean f = true;//谜之定义
		while (f) {//哈哈，不是谜之循环，上面一句的定义是为了进入while循环，顺便定义个布尔类型的变量，作用之后再说
			food[0] = 20 * r.nextInt(31);//nextInt()里的是随机数范围的最大值，最小值是零，乘20是为了让它在蛇能吃到的地方，蛇能走到的坐标是20的倍数
			food[1] = 20 * r.nextInt(23);//刚刚是x坐标，这是y
			f = false;//这个布尔值是刚刚使while循环被执行的条件，现在设置成false不管的话会只执行现在这一次
			for (int i = 0; i < length; i++) {//for循环，i的范围是零到length-1，执行次数的是length次
				if (food[0] == snakeX[i] && food[1] == snakeY[i]) {//其实就是遍历蛇的每一节身体所在的坐标，看看有没有和食物重合的，如果重合了，该怎么办啊T_T
					f = true;//如果重合，怎么是这样啊，这个f看起来不太可靠啊，能行吗
				}
			}
		}//如果重合的话，将无法跳出循环，再次执行循环体，刷新食物坐标，直到不再重合
	}
	// 下面是3个重写大礼包
	@Override // 重写标志 www.bai.com 关键词：@Override
	public void keyPressed(KeyEvent e) {// 按下键的时候调用这个函数，属于用keyListener接口必须要实现的方法
		int keycode = e.getKeyCode();//java语，定义一个整形变量用来接受用户按下方向键的键码值
		if (keycode == KeyEvent.VK_SPACE) {//java语，如果按下去的键的键码值等于空格的键码值，其实意思就是如果按了空格键
			if (isStart) {//就判断游戏是不是开始状态
				isStart = false;//是的话，就宣布，游戏暂停了，当然不是真的暂停，而是后面执行蛇移动的程序看到isSart不是true就不再让蛇的坐标移动了，但是会依然画，哪怕画从动态到禁止的东西就像是突然不画了，就定格了
			} else {//如果游戏本来就是没开始的，就让它继续，跑起来！！！
				if (isFail) {//或许不是游戏没开始，而是游戏早就结束了，没关系，判断一下
					init();//结束的话就清零现在的成绩，带着之前的成绩就是作弊了
				}
				isStart = true;//重新开始
			}
		} else if (keycode == KeyEvent.VK_RIGHT) {//如果按下右方向键
			if (direction != "l") {//就直接转头向右，不是吧，要区分情况啊，如果蛇现在向左的话是不能180°大回头的
				direction = "R";//只要不是向左，其他方向都可以直接转到右
			}
		} else if (keycode == KeyEvent.VK_LEFT) {//按下左
			if (direction != "R") {//只要不是原先向右
				direction = "L";//就可以转
			}
		} else if (keycode == KeyEvent.VK_UP) {//同上
			if (direction != "D") {
				direction = "U";
			}
		} else if (keycode == KeyEvent.VK_DOWN) {//同理
			if (direction != "U") {
				direction = "D";
			}
		}
		
	}
 
	@Override // 重写标志 www.bai.com 关键词：@Override
	public void keyReleased(KeyEvent e) {// 按键按下后弹起时调用，同上
		// 可是要做的都在keyPressed()方法里做完了，就空着，因为必须要实现T_T
	}
 
	@Override // 重写标志 www.bai.com 关键词：@Override
	public void keyTyped(KeyEvent e) {// 输入文本后调用，
		// 同上T_T
	}
 
	public void doLoop() {//来说说游戏动态画面的本质吧，就是静态的画面连续播放，所以执行一次是不够的，要重复循环
		Timer timer = new Timer();//Timer类有个函数
		timer.schedule(new TimerTask() {//函数里有个参数是一个抽象类
			public void run() {//要用这个抽象类就要重写它的构造函数，构造函数是什么，就比如说，你有一个杯子，你能拿他喝可乐，或者咖啡，但决定性的不是这些，
				//重要的是，你现在杯子里有什么？没错，抽象类就是一个什么都能装的杯子，但你能从中喝到什么就取决与它里面装的构造函数是什么
				//那么这个里面装的是啥，是写好任务的记事本，有人会隔一段时间就执行一次这个任务，你写的任务是做饭他就是你的厨师，是开车载你就是你的司机，任务就是这个人的构造函数
		        repaint();//这个函数是JPanel里有的，它会再次调用paint这个绘图方法
		        if (isStart&&!isFail){//java语，如果游戏是开始的(没错121行发出的信号就是它接受的)而且你现在还没吃掉自己
		            for (int i = length-1; i > 0 ; i--) {//就代表你是可以跑的，怎么跑呢，倒一占了前面倒二的位置，倒二占了前面倒三的位置。。。。。直到有人占了第一的位置，那么第一呢
		                snakeX[i] = snakeX[i-1];
		                snakeY[i] = snakeY[i-1];
		            }
		            //第一自己跑了。。。
		            if (direction=="R"){//以屏幕左上角为坐标系原点新建坐标系，求老师让我玩游戏^o^
		            	 snakeX[0] += 20;//如果蛇头方向向右，就x轴正半轴方向跑
		                if (snakeX[0]>620){//跑出界咋办
		                    snakeX[0] = 0;//让它从另一边出来
		                }
		            }
		            else if (direction=="L"){
		                snakeX[0] -= 20;
		                if (snakeX[0]<0){
		                    snakeX[0] = 620;
		                }
		            }
		            else if (direction=="U"){
		                snakeY[0] -= 20;
		                if (snakeY[0]<0){
		                    snakeY[0] = 440;
		                }
		            }
		            else if (direction=="D"){
		                snakeY[0] += 20;
		                if(snakeY[0]>440){
		                    snakeY[0] = 0;
		                }
		            }
		            if (snakeX[0]==food[0]&&snakeY[0]==food[1]){//蛇头坐标如果和食物重合
		                length++;//蛇吃长一节
		                score++;//你得一分
		                refreshFood();//然后食物还得再长出来
		            }
		            for (int i = 1; i < length; i++) {//遍历除蛇头以为外的蛇身部分
		                if (snakeX[0]==snakeX[i]&&snakeY[0]==snakeY[i]){//如果蛇头和蛇身某一处重合，
		                    isFail = true;//就把自己吃掉了
		                    isStart = false;//gameover                        
		                }
		            }
				}
			}
		}, 0, 50);//这两个参数一个是等待多久开始执行，另一个是间隔多久执行一次
	}
}
