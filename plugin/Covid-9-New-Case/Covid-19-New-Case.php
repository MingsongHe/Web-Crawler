<?php
/**
 * @package Covid-19 New Cases
 * @version 1.0.0
 */
/*
Plugin Name: Covid-19 New Case（伊麦阳光服务）
Plugin URI: https://bilingualplan.com/zh/covid-19-newcase-cn/
Description: 这是一个练习插件。这个插件接收上传来的变量值，然后保存变量值（第一次自动建立变量）在数据库的 option 表单里，供网站的PHP程序调取，显示在页面或者别的地方。上传的完成是使用部署在线下的一个网络爬虫程序（Python程序，在树莓派上定时运行）爬取新加坡卫生部网站公布的最新Covid-19感染人数数据，然后以正确的格式上传。
Version: 1.0.0
Author URI: https://bilingualplan.com/zh/home-zhcn/
Author: EMS SUNLIGHT SERVICE （伊麦阳光服务）
*/

/*
//$newcaseNumber=isset($_GET['newcaseNumber'])?$_GET['newcaseNumber']:"";
$newcaseNumber=$_GET['newcaseNumber'];
if($newcaseNumber!="") echo "Today increase 是: ".$newcaseNumber;
*/

$newcaseNumber=$_GET['newcaseNumber'];
$newcaseDate=$_GET['newcaseDate'];
$localPCR=$_GET['localPCR'];
$localART=$_GET['localART'];
$importedPCR=$_GET['importedPCR'];
$importedART=$_GET['importedART'];
if($newcaseNumber!=""){

	update_option('newcaseNo',$newcaseNumber);
	update_option('newcaseDate',$newcaseDate);
	update_option('localPCR',$localPCR);
	update_option('localART',$localART);
	update_option('importedPCR',$importedPCR);
	update_option('importedART',$importedART);
}

$datacollection=$_GET['datacollection'];
if($datacollection!=""){
    $wpdb -> update('ufq_iotdata', array('data_collection' => $datacollection), array('id' => 2));
}

$video_position=$_GET['video_position'];
if($video_position!=""){
    $wpdb -> update('ufq_iotdata', array('video_position' => $video_position), array('id' => 2));
}

/*
改变中文的文章标题
*/
function change_title_if_civid19_cn( $title, $id = null ) {
    global $newcaseNumber;
 
    if ( in_category('Covid-19-cn', $id ) ) {
        return (get_option('newcaseDate'))."  ".新增感染人数：.get_option('newcaseNo');
    }
 
    return $title;
}
add_filter( 'the_title', 'change_title_if_civid19_cn', 9, 2 );

/*
改变英文的文章标题
*/
function change_title_if_civid19( $title, $id = null ) {
    global $newcaseNumber;
 
    if ( in_category('Covid-19', $id ) ) {
        return (get_option('newcaseDate'))."  ".newcases：.get_option('newcaseNo');
    }
 
    return $title;
}

add_filter( 'the_title', 'change_title_if_civid19', 10, 2 );

//一个小练习：发布文章时，通过电子邮件发给朋友提示

function email_friends( $post_ID )  
{
   $friends = '1010372463@qq.com, cddy7@msn.com';
   wp_mail( $friends, "HE MINGSONG's blog updated", 'I just put something on my blog: https://bilingualplan.com/en/blog/' );

   return $post_ID;
}
add_action( 'publish_post', 'email_friends' );//在Plugin API/Action Reference 上查看动作hook列表

