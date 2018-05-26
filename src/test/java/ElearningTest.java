import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.*;

public class ElearningTest {
    // WebDriver驱动路径
    private final String DRIVER_PATH = "/Users/lvjiawei/Documents/softwaretest/hw3/chromedriver";
    // 学号
    private final String USERNAME = "515030910036";
    // 密码
    private final String PASSWORD = "123456";
    // 上传文件的路径
    private final String FILE_PATH = "/Users/lvjiawei/Documents/softwaretest/hw3/favicon.png";

    private WebDriver driver;
    /**
     * 进入个人信息页面
     * @param  driver WebDriver
     * @return driver WebDriver
     */
    private WebDriver gotoUserProfile(WebDriver driver) {
        // 打开网页
        driver.get("http://elearning.se.sjtu.edu.cn/login.asp");

        // 输入用户名
        driver.findElement(By.name("loginname")).sendKeys(USERNAME);

        // 输入密码
        driver.findElement(By.name("password")).sendKeys(PASSWORD);

        // 登录
        driver.findElement(By.className("commandbutton")).click();

        // 进入个人资料
        driver.findElement(By.className("topfade")).findElements(By.className("mainmenu")).get(0).click();

        return driver;
    }

    /**
     * 生成随机字符串
     * @param length 字符串长度
     * @return string 字符串
     */
    private static String getRandomString(int length) {
        String str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random random = new Random();
        StringBuffer sb = new StringBuffer();

        for(int i = 0 ; i < length; ++i){
            int number = random.nextInt(62);//[0,62)

            sb.append(str.charAt(number));
        }
        return sb.toString();
    }

    /**
     * 测试密码合法性
     * @param driver WebDriver
     * @param test1 密码1
     * @param test2 密码2
     * @return driver WebDriver
     */
    private WebDriver testPassword( WebDriver driver, String test1, String test2) {
        // 获取密码输入框
        WebElement password1 = driver.findElement(By.xpath("//input[@name='txtPassword']"));
        WebElement password2 = driver.findElement(By.xpath("//input[@name='txtRePassword']"));

        // 获取提交按钮
        WebElement submitBtn = driver.findElement(By.xpath("//a[@href='javascript:funUptdata();']"));

        // 验证密码合法性
        password1.clear();
        password1.sendKeys(test1);
        password2.clear();
        password2.sendKeys(test2);
        System.out.println("pwd1=" + password1.getAttribute("value") + " pwd2=" + password2.getAttribute("value"));
        submitBtn.click();
        String alertMsg = driver.switchTo().alert().getText();
        if (alertMsg != null) {
            System.out.println("Message: " + alertMsg);
            driver.switchTo().alert().accept();
            Assert.assertTrue(true);
        } else {
            Assert.fail();
        }
        return driver;
    }

    /**
     * 用例开始前打印
     */
    @BeforeClass
    public void beforeClass() {
        System.out.println("[用例开始执行]");

        // 设置驱动位置
        System.setProperty("webdriver.chrome.driver", DRIVER_PATH);

        // 启动Chrome浏览器
        driver = new ChromeDriver();

        // 进入个人资料
        driver = gotoUserProfile(driver);
    }

    /**
     * 用例结束后打印
     */
    @AfterClass
    public void afterClass(){
        System.out.println("[用例运行结束]");
        driver.quit();
    }

    /**
     * 测试页面上所有超链接是否可用
     */
    @Test
    public void testAllLinks() {
        // 获取所有<a>标签
        List<WebElement> linkList = driver.findElements(By.tagName("a"));

        // 提取所有超链接
        Iterator<WebElement> iterator = linkList.iterator();
        List<String> urlList = new ArrayList<>();
        while (iterator.hasNext()) {
            WebElement webElement = iterator.next();
            String href = webElement.getAttribute("href");
            if (href == null || href.equals(driver.getCurrentUrl()) || !href.contains("http")) iterator.remove();
            else urlList.add(href);
        }

        // 测试URL是否能正常打开和后退回正确页面
        String profileUrl = "http://elearning.se.sjtu.edu.cn/profile.asp";
        for (String url : urlList) {
            driver.get(url);
            System.out.println(url + " " + driver.getTitle());
            Assert.assertEquals(driver.getTitle(), "e-Learning platform -- LEO-Pro");
            driver.navigate().back();
            Assert.assertEquals(driver.getCurrentUrl(), profileUrl);
        }


    }

    /**
     * 测试页面上所有文本输入框是否可用
     */
    @Test
    public void testAllInputs() {
        // 获取所有文本输入框
        List<WebElement> inputList = driver.findElements(By.xpath("//input[@type='text']"));

        // 随机输入文本，测试是否可用
        for (WebElement webElement : inputList) {
            int length = new Random().nextInt(4) + 1;
            String randomString = getRandomString(length);

            webElement.clear();
            webElement.sendKeys(randomString);
            String value = webElement.getAttribute("value");

            System.out.println("input value=" + value + " randomString=" + randomString);
            Assert.assertEquals(value, randomString);
        }


    }

    /**
     * 测试页面上所有单选按钮是否可用
     */
    @Test
    public void testAllRadios() {
        // 获取所有input标签
        List<WebElement> inputList = driver.findElements(By.tagName("input"));

        // 提取单选按钮
        Iterator<WebElement> iterator = inputList.iterator();
        while (iterator.hasNext()) {
            WebElement webElement = iterator.next();
            String type = webElement.getAttribute("type");
            String disabled = webElement.getAttribute("disabled");
            if (disabled == null) disabled = "false";
            if (!type.equals("radio") || disabled.equals("true")) iterator.remove();
        }

        // 测试单选按钮是否可用
        for (WebElement webElement : inputList) {
            webElement.click();
            System.out.println("name=" + webElement.getAttribute("name") + " value=" + webElement.getAttribute("value"));
            Assert.assertTrue(webElement.isSelected());
        }


    }

    /**
     * 测试页面上所有选择框是否可用
     */
    @Test
    public void testAllSelects() {
        // 获取所有select标签
        List<WebElement> inputList = driver.findElements(By.tagName("select"));

        // 保存为Select对象
        List<Select> selectList = new ArrayList<>();
        for (WebElement webElement : inputList) {
            selectList.add(new Select(webElement));
        }

        // 测试select框是否可用
        for (Select select : selectList) {
            int randomOption = new Random().nextInt(select.getOptions().size());
            select.selectByIndex(randomOption);
            String selectedOption = select.getFirstSelectedOption().getText();
            System.out.println("selected option=" + selectedOption);
            Assert.assertNotNull(selectedOption);
        }


    }

    /**
     * 测试页面上所有多选框是否可用
     */
    @Test
    public void testAllCheckboxs() {
        // 获取所有多选框
        List<WebElement> checkboxList = driver.findElements(By.xpath("//input[@type='checkbox']"));

        // 测试多选框是否可用
        for (WebElement webElement : checkboxList) {
            webElement.click();
            System.out.println(webElement.getAttribute("name") + " is selected: " + webElement.isSelected());
            Assert.assertTrue(webElement.isSelected());
        }


    }

    /**
     * 测试页面上所有文件上传是否可用
     */
    @Test
    public void testAllUploadFiles() {
        // 获取所有文件上传
        List<WebElement> fileUploadList = driver.findElements(By.xpath("//input[@type='file']"));

        for (WebElement webElement : fileUploadList) {
            webElement.sendKeys(FILE_PATH);
            System.out.println("file path=" + webElement.getAttribute("value"));
            Assert.assertNotNull(webElement.getAttribute("value"));
        }


    }

    /**
     * 测试姓名输入合法性验证
     */
    @Test
    public void testNameValidator() {
        driver = gotoUserProfile(driver);
        // 获取姓名输入框
        WebElement name1 = driver.findElement(By.xpath("//input[@name='txtNameGb1']"));
        WebElement name2 = driver.findElement(By.xpath("//input[@name='txtNameGb2']"));

        // 获取提交按钮
        WebElement submitBtn = driver.findElement(By.xpath("//a[@href='javascript:funUptdata();']"));

        // 验证姓名输入合法性
        // 姓名为空
        name1.clear();
        name1.sendKeys("");
        name2.clear();
        name2.sendKeys("");
        System.out.println("value=" + name1.getAttribute("value"));
        submitBtn.click();
        String alertMsg = driver.switchTo().alert().getText();
        if (alertMsg != null) {
            System.out.println("Message: " + alertMsg);
            driver.switchTo().alert().accept();
            Assert.assertTrue(true);
        } else {
            Assert.fail();
        }


    }

    /**
     * 测试密码输入合法性验证
     */
    @Test
    public void testPasswordValidator() {
        driver = gotoUserProfile(driver);
        // 密码为空
        driver = testPassword(driver, "", "");
        // 密码长度不足
        driver = testPassword(driver, "123", "123");
        // 两次密码不一致
        driver = testPassword(driver, "123456", "1234567");

    }

}
