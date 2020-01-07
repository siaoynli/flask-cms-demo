/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : flask-login

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 06/09/2018 17:15:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admins
-- ----------------------------
DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nick_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `chinese_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sex` smallint(6) NULL DEFAULT NULL,
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qq` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `remarks` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_ip` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_time` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_count` int(11) NULL DEFAULT NULL,
  `is_super` smallint(6) NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_admins_email`(`email`) USING BTREE,
  UNIQUE INDEX `ix_admins_name`(`name`) USING BTREE,
  UNIQUE INDEX `ix_admins_phone`(`phone`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `ix_admins_is_active`(`is_active`) USING BTREE,
  INDEX `ix_admins_is_delete`(`is_delete`) USING BTREE,
  CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admins
-- ----------------------------
INSERT INTO `admins` VALUES (1, 0, 1, NULL, '2018-08-29 14:27:13', 'admin', 'admin@126.com', 'pbkdf2:sha256:50000$FZqGtAvo$dff9b81a4525a344873890db245d7e29d1370c3fb5cf54867e8eed2c7afea41f', 'admin1', '管理员', '/uploads/images/2018-09-03/7f9e1246c4caf9a740b0500318539a43.jpg', 2, '13516872343', '120235331', '', '127.0.0.1', '2018-09-06 14:56:51', 34, 0, 1);
INSERT INTO `admins` VALUES (2, 0, 1, '2018-07-24 14:36:20', '2018-09-03 17:01:06', 'addsf', 'sdfsdf@126.com', 'pbkdf2:sha256:50000$JO5Z1xxx$24dc150b5857f27c3bf80ea8e459d582500be5b782b3ef8bda6103492a88b07f', 'dsfdsf', '是的发', '/uploads/images/2018-09-03/903eb6bfa3e48ff37e373dd37d768428.jpg', 2, '18906715596', '23424324', 'sdfd', '', '', 0, 0, 1);
INSERT INTO `admins` VALUES (5, 0, 1, '2018-07-24 14:43:36', '2018-07-25 10:58:54', 'lixiaoyun', 'dfhdskhf@126.com', 'pbkdf2:sha256:50000$rK3mJVzR$0db77798e03f31b7b06881456a0989c5f9ece111d0bb1bdb850a710958d0d447', 'lixiaoyun', '打发斯', '/static/admin/images/guest.png', 1, '13516872342', '120235331', 'dfdsf', '', '', 0, 0, 1);
INSERT INTO `admins` VALUES (6, 1, 1, '2018-07-24 14:55:29', '2018-07-25 10:45:53', 'siaoynli', 'xdfds@32432.com', 'pbkdf2:sha256:50000$80lnrKHv$f6f605797b7a89ea3cd63406c71d667b0c55ddac8d079b02c87f258f9b9b2c6f', 'dfds123', '沙发', '/static/admin/images/guest.png', 1, '18906715574', '252996708', 'sdfdsf', '127.0.0.1', '2018-07-24 15:08:52', 1, 0, 7);
INSERT INTO `admins` VALUES (7, 1, 1, '2018-07-25 11:05:44', '2018-07-25 11:05:54', 'dsf', 'dfsdfs@126.com', 'pbkdf2:sha256:50000$lAMVTEKm$243c7acd4310c9e09f7ab0af1c88376763852f56779f3c3ed9a708296da33a4b', 'sdfsdf', '大杀四方', '/static/admin/images/guest.png', 2, '18906715591', '', '', '', '', 0, 0, 1);

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('9516d9424ae9');

-- ----------------------------
-- Table structure for columns
-- ----------------------------
DROP TABLE IF EXISTS `columns`;
CREATE TABLE `columns`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `title` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `keyword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `column_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `thumb_image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `external_link` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `pid` int(11) NULL DEFAULT NULL,
  `target` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  INDEX `ix_columns_is_active`(`is_active`) USING BTREE,
  INDEX `ix_columns_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of columns
-- ----------------------------
INSERT INTO `columns` VALUES (1, 0, 1, NULL, NULL, '网站首页', 'sdf', 'sdf', NULL, NULL, NULL, NULL, 1, 0, NULL);
INSERT INTO `columns` VALUES (2, 0, 1, NULL, NULL, '文章', NULL, NULL, NULL, NULL, NULL, NULL, 2, 1, NULL);
INSERT INTO `columns` VALUES (3, 0, 1, NULL, NULL, '随笔', NULL, NULL, NULL, NULL, NULL, NULL, 3, 2, NULL);
INSERT INTO `columns` VALUES (4, 0, 1, NULL, NULL, '札记', NULL, NULL, NULL, NULL, NULL, NULL, 3, 2, NULL);
INSERT INTO `columns` VALUES (5, 0, 1, NULL, NULL, '图片', NULL, NULL, NULL, NULL, NULL, NULL, 2, 1, NULL);

-- ----------------------------
-- Table structure for document_tag
-- ----------------------------
DROP TABLE IF EXISTS `document_tag`;
CREATE TABLE `document_tag`  (
  `document_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`document_id`, `tag_id`) USING BTREE,
  INDEX `tag_id`(`tag_id`) USING BTREE,
  CONSTRAINT `document_tag_ibfk_1` FOREIGN KEY (`document_id`) REFERENCES `documents` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `document_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for documents
-- ----------------------------
DROP TABLE IF EXISTS `documents`;
CREATE TABLE `documents`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `keyword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `external_link` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `published_at` datetime(0) NULL DEFAULT NULL,
  `thumb_image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `author` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `attribute` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `target` tinyint(1) NULL DEFAULT NULL,
  `click` int(11) NULL DEFAULT NULL,
  `open_comment` tinyint(1) NULL DEFAULT NULL,
  `attach_file` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `attach_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_show` tinyint(1) NULL DEFAULT NULL,
  `password_txt` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `column_id` int(11) NULL DEFAULT NULL,
  `admin_id` int(11) NULL DEFAULT NULL,
  `uuid` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `editor` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `source` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `source_link` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sub_title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_original` tinyint(1) NULL DEFAULT NULL,
  `tags` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `user_group` tinyint(1) NULL DEFAULT NULL,
  `use_title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  UNIQUE INDEX `ix_documents_uuid`(`uuid`) USING BTREE,
  INDEX `admin_id`(`admin_id`) USING BTREE,
  INDEX `column_id`(`column_id`) USING BTREE,
  INDEX `ix_documents_is_active`(`is_active`) USING BTREE,
  INDEX `ix_documents_is_delete`(`is_delete`) USING BTREE,
  INDEX `ix_documents_tags`(`tags`) USING BTREE,
  CONSTRAINT `documents_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `documents_ibfk_2` FOREIGN KEY (`column_id`) REFERENCES `columns` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of documents
-- ----------------------------
INSERT INTO `documents` VALUES (1, 0, 1, NULL, '2018-09-03 16:49:18', '美联航更改涉台标注 “不情愿”的新证据又被爆料fghfgh', '关键字111111', '描述22211111', '如你所见，layDate 在 layui 2.0 的版本中迎来一次重生。无论曾经它给你带来过多么糟糕的体验，从今往后，所有的旧坑都将弥合。全面重写的 layDate 包含了大量的更新，其中主要以：年选择器、年月选择器、日期选择器、时间选择器、日期时间选择器 五种类型的选择方式为基本核心，并且均支持范围选择（即双控件）。内置强劲的自定义日期格式解析和合法校正机制111', 'http://www.baidu.com', '2018-08-30 11:04:48', '/uploads/images/2018-09-03/cc3f1751883fc8040e38c48881573719.jpg', 'admin', 'R,T,H', '', 1, 90, 1, '/uploads/attach/2018-09-03/02fd2bde6bea1db7dcc33d9bb2fcb840.zip', 'ueditor-emotion.zip', 1, '', 5, 1, 'artilce-1', 'sddsfdsf', '', '', 'dddd', 1, '', 0, NULL);
INSERT INTO `documents` VALUES (3, 0, 1, '2018-09-03 10:57:39', '2018-09-03 16:49:15', 'Ceshi', 'ceshi洒洒地撒', 'ceshi洒洒地撒', 'ceshi洒洒地撒', '', '2018-09-03 10:55:36', '/uploads/images/2018-09-03/83504221b26219f4f625db39056d0e26.jpg', '管理员', '', '', 1, 0, 1, '', '', 0, '', 4, 1, 'sadas', '', '', '', '', 1, '', 0, NULL);
INSERT INTO `documents` VALUES (4, 0, 1, '2018-09-03 11:06:20', '2018-09-03 16:49:11', 'sdfsdf', 'sffdsfsf', 'sdfdsfdsf', 'sdfsdfdsf', '', '2018-09-03 11:06:12', '/uploads/images/2018-09-03/a62d21558deb3ace4f80af61cccd96e2.jpg', '管理员', 'R,T,H', '', 1, 0, 1, '', '', 0, '', 2, 1, '11111', '', '', '', '', 1, '', 0, NULL);
INSERT INTO `documents` VALUES (5, 0, 1, '2018-09-03 11:23:08', '2018-09-03 16:49:06', '杭州网媒体管理系统', 'dfcvxcv', '管理员3213213', '管理员1222212', '', '2018-09-03 11:23:08', '/uploads/images/2018-09-03/c857f5bd351578ff122d7b7628f0c5a9.jpg', '管理员', '', '', 1, 100, 1, '', '', 1, '', 3, 1, '2749bfba-456e-4b38-a597-6a886999d0a0', '管理员3', '管理员1', '', '', 1, '', 0, NULL);
INSERT INTO `documents` VALUES (6, 0, 1, '2018-09-03 11:23:46', '2018-09-03 16:49:02', '杭州网媒体管理系统22200', 'sdfasdsad', 'sdfsdf', 'sdasdasd', '', '2018-09-03 11:23:32', '/uploads/images/2018-09-03/a1a5b2966e1378c2fe72e2a8a5c7e666.jpg', '管理员', '', '', 1, 200, 1, '', '', 1, '12313', 3, 1, '0784d6f7-2cf8-489c-aa9e-aad1f129eb8e', 'asdasd', '', '', '1123213', 1, '', 0, NULL);
INSERT INTO `documents` VALUES (7, 0, 1, '2018-09-03 11:24:25', '2018-09-05 16:10:37', '朱妤223232136', '美女  独孤', 'ww', 'sadasd', 'http://baidu.com', '2018-09-05 15:44:49', '/uploads/images/2018-09-05/da7c483bbcab5d01878eca82da24773b.jpg', '管理员', 'R,T', '', 1, 100, 1, '1111', 'fdgdfg', 0, '', 4, 1, 'a1b29ff2-439d-412b-9013-f667f6a82dbf', '111', 'ssf', 'http://baidu.com', '', 1, '', 0, NULL);

-- ----------------------------
-- Table structure for focuses
-- ----------------------------
DROP TABLE IF EXISTS `focuses`;
CREATE TABLE `focuses`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `title` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `link` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `thumb_image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `target` tinyint(1) NULL DEFAULT NULL,
  `column_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  INDEX `column_id`(`column_id`) USING BTREE,
  INDEX `ix_focuses_is_active`(`is_active`) USING BTREE,
  INDEX `ix_focuses_is_delete`(`is_delete`) USING BTREE,
  CONSTRAINT `focuses_ibfk_1` FOREIGN KEY (`column_id`) REFERENCES `columns` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of focuses
-- ----------------------------
INSERT INTO `focuses` VALUES (1, 0, 1, NULL, '2018-08-30 11:29:59', 'dsf123', 'oik00', '', '/uploads/images/2018-07-30/1e0db4a4-76ad-4930-aa10-bd204fc1ca51.jpg', 1, 1, 1);
INSERT INTO `focuses` VALUES (3, 0, 1, '2018-07-30 15:24:20', '2018-08-02 14:40:23', 'sdfasd', 'asdasd', '', '/uploads/images/2018-07-30/79bbd8d3-b19d-4894-957c-958f28ac2622.jpg', 3, 1, 1);
INSERT INTO `focuses` VALUES (4, 0, 1, '2018-07-30 15:25:11', '2018-08-02 14:40:26', 'asdasd', 'asdsad', '', '/uploads/images/2018-07-30/9d707ce0-6109-40ca-86d8-4005102b03a8.jpg', 3, 1, 1);
INSERT INTO `focuses` VALUES (6, 0, 1, '2018-07-30 15:26:50', '2018-09-05 14:43:33', 'dfdsf', 'sdfsdf', '', '/uploads/images/2018-09-05/25c2c16b2cab812395e936ea8e37319b.jpg', 4, 1, 1);

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `label` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `label`(`label`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_groups_is_active`(`is_active`) USING BTREE,
  INDEX `ix_groups_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of groups
-- ----------------------------
INSERT INTO `groups` VALUES (1, 0, 0, NULL, NULL, '游客', '游客');

-- ----------------------------
-- Table structure for guestbooks
-- ----------------------------
DROP TABLE IF EXISTS `guestbooks`;
CREATE TABLE `guestbooks`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `ip` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `published_at` datetime(0) NULL DEFAULT NULL,
  `pid` int(11) NULL DEFAULT NULL,
  `open_comment` tinyint(1) NULL DEFAULT NULL,
  `label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `user_type` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `good` int(11) NULL DEFAULT NULL,
  `read` int(11) NULL DEFAULT NULL,
  `root_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_guestbooks_is_active`(`is_active`) USING BTREE,
  INDEX `ix_guestbooks_is_delete`(`is_delete`) USING BTREE,
  INDEX `ix_guestbooks_root_id`(`root_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of guestbooks
-- ----------------------------
INSERT INTO `guestbooks` VALUES (1, 0, 1, '2018-08-08 15:45:12', '2018-08-08 15:55:00', '测试留言1234很好', 2, 'test001', '127.0.0.1', '2018-08-08 14:58:27', 0, 1, NULL, 'user', 1, 0, '0');
INSERT INTO `guestbooks` VALUES (2, 0, 1, '2018-08-08 15:45:12', '2018-08-08 16:00:05', 'demo2', 1, 'admin', '127.0.0.1', '2018-08-08 15:45:12', 1, 1, '', 'admin', 1, 0, '0-1');
INSERT INTO `guestbooks` VALUES (3, 0, 1, '2018-08-08 16:48:49', '2018-08-28 11:26:53', '2343269', 2, 'test001', '127.0.0.1', '2018-08-08 16:49:27', 2, 1, NULL, 'user', 1, 0, '0-1-2');
INSERT INTO `guestbooks` VALUES (4, 0, 1, '2018-08-08 17:05:46', '2018-08-28 13:48:52', 'haha3', 1, 'admin', '127.0.0.1', '2018-08-08 17:05:46', 3, 1, '', 'admin', 0, 0, '0-1-2-3');
INSERT INTO `guestbooks` VALUES (5, 0, 1, '2018-08-08 17:07:26', '2018-08-29 16:00:52', '测试', 1, 'admin', '127.0.0.1', '2018-08-08 17:07:26', 3, 1, '', 'admin', 1, 0, '0-1-2-3');
INSERT INTO `guestbooks` VALUES (6, 0, 1, '2018-08-28 14:03:22', '2018-08-29 16:00:53', 'sdfdsf', 1, 'admin', '127.0.0.1', '2018-08-28 14:03:22', 1, 1, '', 'admin', 0, 0, '0-1');
INSERT INTO `guestbooks` VALUES (7, 0, 1, '2018-08-28 14:04:05', '2018-08-28 14:04:07', '687658', 2, 'test001', '127.0.0.1', '2018-08-28 14:04:17', 6, 1, NULL, 'user', 0, 0, '0-1-6');
INSERT INTO `guestbooks` VALUES (8, 0, 1, '2018-08-28 14:28:27', '2018-08-30 11:30:27', 'sdfdsfsdfdsf12222', 1, 'admin', '127.0.0.1', '2018-08-28 14:28:27', 1, 1, '', 'admin', 10, 0, '0-1');

-- ----------------------------
-- Table structure for links
-- ----------------------------
DROP TABLE IF EXISTS `links`;
CREATE TABLE `links`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `site_url` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `logo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `site_admin` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `site_admin_email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `site_admin_qq` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `site_admin_phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `home_show` tinyint(1) NULL DEFAULT NULL,
  `site_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `site_name`(`site_name`) USING BTREE,
  INDEX `ix_links_is_active`(`is_active`) USING BTREE,
  INDEX `ix_links_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of links
-- ----------------------------
INSERT INTO `links` VALUES (1, 0, 1, '2018-08-02 14:31:32', '2018-08-02 15:00:22', 'http://baidu.com', '', '/uploads/images/2018-08-02/931a522f-85dc-4eb0-a39c-bc13357784e3.jpg', '', 'admin@126.com', '252996708', '13516872342', 6, 1, 'dsfdsf123');
INSERT INTO `links` VALUES (2, 0, 1, '2018-08-02 14:41:47', '2018-08-02 15:07:06', 'http://127.0.0.1:5000/admin/link', 'sdfsdf', '', 'dsf', 'afsdafd@126.com', '123456', '13516872356', 1, 1, '杭州网媒体管理系统1');
INSERT INTO `links` VALUES (3, 0, 1, '2018-08-02 15:12:16', '2018-08-02 15:12:16', 'http://127.0.0.1:5000/admin/index', 'http://127.0.0.1:5000/admin/index', '', '', '', '', '', 1, 1, '杭州网媒体管理系统');
INSERT INTO `links` VALUES (4, 0, 1, '2018-08-02 15:12:31', '2018-08-29 16:07:32', 'http://127.0.0.1:5000/admin/index', 'http://127.0.0.1:5000/admin/index', '/uploads/images/2018-08-02/fbf35341-f1b5-441e-af43-5d41c5645a34.jpg', '', '', '', '', 1, 1, '杭州网媒体管理系统2');

-- ----------------------------
-- Table structure for mails
-- ----------------------------
DROP TABLE IF EXISTS `mails`;
CREATE TABLE `mails`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `mail_server` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `port` int(11) NULL DEFAULT NULL,
  `link_model` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_mails_is_active`(`is_active`) USING BTREE,
  INDEX `ix_mails_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of mails
-- ----------------------------
INSERT INTO `mails` VALUES (1, 0, 1, '2018-07-25 16:31:38', '2018-07-27 15:00:07', 'smtp.qq.com', 465, 'ssl', '120235331@qq.com', 'dwmtcdjpfylxcagh');

-- ----------------------------
-- Table structure for menus
-- ----------------------------
DROP TABLE IF EXISTS `menus`;
CREATE TABLE `menus`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `pid` int(11) NULL DEFAULT NULL,
  `icon` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `endpoint_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `target` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_menus_is_active`(`is_active`) USING BTREE,
  INDEX `ix_menus_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of menus
-- ----------------------------
INSERT INTO `menus` VALUES (1, 0, 1, NULL, '2018-09-05 16:30:29', '设置', '设置', 1, 0, 'layui-icon-set', '', 1);
INSERT INTO `menus` VALUES (4, 0, 1, NULL, '2018-09-06 15:33:46', '系统设置', '系统设置', 1, 0, 'layui-icon-cellphone', '', 1);
INSERT INTO `menus` VALUES (5, 0, 1, NULL, '2018-09-05 17:31:03', '导航设置', '导航设置', 2, 4, 'layui-icon-set', 'menu_index', 1);
INSERT INTO `menus` VALUES (6, 0, 1, NULL, '2018-09-06 15:33:52', '我的设置', '我的设置', 1, 0, '', '', 1);
INSERT INTO `menus` VALUES (7, 0, 1, NULL, NULL, '基本资料', '基本资料', 2, 6, '', 'admin_profile', 1);
INSERT INTO `menus` VALUES (8, 0, 1, NULL, NULL, '修改头像', '修改头像', 2, 6, '', 'admin_edit_avatar', 1);
INSERT INTO `menus` VALUES (9, 0, 1, NULL, NULL, '修改密码', '修改密码', 2, 6, '', 'admin_edit_password', 1);

-- ----------------------------
-- Table structure for messages
-- ----------------------------
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ip` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `published_at` datetime(0) NULL DEFAULT NULL,
  `pid` int(11) NULL DEFAULT NULL,
  `label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_messages_is_active`(`is_active`) USING BTREE,
  INDEX `ix_messages_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for notes
-- ----------------------------
DROP TABLE IF EXISTS `notes`;
CREATE TABLE `notes`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `start_date` date NULL DEFAULT NULL,
  `end_date` date NULL DEFAULT NULL,
  `admin_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `admin_id`(`admin_id`) USING BTREE,
  INDEX `ix_notes_is_active`(`is_active`) USING BTREE,
  INDEX `ix_notes_is_delete`(`is_delete`) USING BTREE,
  CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of notes
-- ----------------------------
INSERT INTO `notes` VALUES (1, 0, 1, '2018-08-02 15:56:41', '2018-08-29 15:36:18', 'dfdsfsdf10', 1, '2018-08-08', '2018-08-31', 1);
INSERT INTO `notes` VALUES (2, 0, 1, '2018-08-02 15:58:08', '2018-08-29 16:07:43', '楼主近日在Windows server 2016的Hyper-V下建了一个虚拟机，然后装了LEDE软路由，本来主板自带两个网卡，一个用来wan拨号，一个用来lan接交换机，正常上网。昨日深水宝入手一张4口PCIE的网卡，插上去后系统直接识别。于是我就在虚拟机交换机设置里新建了4个连接外网的网卡并添加到了LEDE。然后在LEDE设置里把这4个网口添加到Lan里。保存应用后，原来的Lan口可以继续使用，但是PCIE网卡上的4个口子。连线无法上网，求正确配置。11', 2, '2018-08-29', '2018-08-30', 1);
INSERT INTO `notes` VALUES (3, 1, 1, '2018-08-02 16:05:32', '2018-08-29 15:01:23', 'sdfdsf9', 1, '2018-08-06', '2018-08-23', 1);

-- ----------------------------
-- Table structure for permissions
-- ----------------------------
DROP TABLE IF EXISTS `permissions`;
CREATE TABLE `permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `endpoint_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `label` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `level` int(11) NULL DEFAULT NULL,
  `menu_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `endpoint_name`(`endpoint_name`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_permissions_is_active`(`is_active`) USING BTREE,
  INDEX `ix_permissions_is_delete`(`is_delete`) USING BTREE,
  INDEX `menu_id`(`menu_id`) USING BTREE,
  CONSTRAINT `permissions_ibfk_1` FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permissions
-- ----------------------------
INSERT INTO `permissions` VALUES (1, 0, 1, NULL, NULL, '导航列表', 'menu_index', '导航列表', 0, 5);
INSERT INTO `permissions` VALUES (2, 0, 1, NULL, NULL, '添加导航', 'menu_create', '添加导航', 0, 5);
INSERT INTO `permissions` VALUES (3, 0, 1, NULL, NULL, '保存导航', 'menu_store', '保存导航', 0, 5);
INSERT INTO `permissions` VALUES (4, 0, 1, NULL, NULL, '编辑导航', 'menu_edit', '编辑导航', 0, 5);
INSERT INTO `permissions` VALUES (5, 0, 1, NULL, '2018-07-27 09:59:04', '更新导航', 'menu_update', '更新导航', 0, 5);
INSERT INTO `permissions` VALUES (6, 0, 1, NULL, '2018-07-27 09:59:03', '删除导航', 'menu_delete', '删除导航', 0, 5);
INSERT INTO `permissions` VALUES (7, 0, 1, NULL, '2018-07-27 09:59:02', '修改基本资料', 'admin_profile', '修改基本资料', 0, 7);
INSERT INTO `permissions` VALUES (8, 0, 1, NULL, '2018-07-30 14:34:44', '修改密码', 'admin_edit_password', '修改密码', 0, 9);
INSERT INTO `permissions` VALUES (9, 0, 1, NULL, '2018-09-06 16:05:12', '修改头像', 'admin_edit_avatar', '修改头像', 0, 8);

-- ----------------------------
-- Table structure for role_permission
-- ----------------------------
DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE `role_permission`  (
  `permission_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`permission_id`, `role_id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `role_permission_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `role_permission_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role_permission
-- ----------------------------
INSERT INTO `role_permission` VALUES (1, 1);
INSERT INTO `role_permission` VALUES (2, 1);
INSERT INTO `role_permission` VALUES (3, 1);
INSERT INTO `role_permission` VALUES (4, 1);
INSERT INTO `role_permission` VALUES (5, 1);
INSERT INTO `role_permission` VALUES (6, 1);
INSERT INTO `role_permission` VALUES (7, 1);
INSERT INTO `role_permission` VALUES (8, 1);
INSERT INTO `role_permission` VALUES (9, 1);
INSERT INTO `role_permission` VALUES (1, 7);
INSERT INTO `role_permission` VALUES (2, 7);
INSERT INTO `role_permission` VALUES (3, 7);
INSERT INTO `role_permission` VALUES (4, 7);
INSERT INTO `role_permission` VALUES (5, 7);
INSERT INTO `role_permission` VALUES (6, 7);
INSERT INTO `role_permission` VALUES (1, 8);
INSERT INTO `role_permission` VALUES (2, 8);
INSERT INTO `role_permission` VALUES (3, 8);
INSERT INTO `role_permission` VALUES (4, 8);
INSERT INTO `role_permission` VALUES (5, 8);
INSERT INTO `role_permission` VALUES (6, 8);
INSERT INTO `role_permission` VALUES (7, 8);
INSERT INTO `role_permission` VALUES (8, 8);

-- ----------------------------
-- Table structure for roles
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `label` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `label`(`label`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_roles_is_active`(`is_active`) USING BTREE,
  INDEX `ix_roles_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES (1, 0, 1, NULL, NULL, '超级管理员', '超级管理员');
INSERT INTO `roles` VALUES (7, 0, 1, NULL, NULL, '普通管理员', '普通管理员1');
INSERT INTO `roles` VALUES (8, 1, 1, NULL, NULL, 'dsfdsf', 'sdfdsf666');

-- ----------------------------
-- Table structure for systems
-- ----------------------------
DROP TABLE IF EXISTS `systems`;
CREATE TABLE `systems`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `site_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `keyword` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `icp` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `census_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `copyright` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `upload_path` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `water_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `images_water` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `txt_water` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `txt_water_size` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `txt_water_font` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `txt_water_color` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `images_size` int(11) NULL DEFAULT NULL,
  `images_extensions` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `images_max_width` int(11) NULL DEFAULT NULL,
  `images_max_height` int(11) NULL DEFAULT NULL,
  `media_size` int(11) NULL DEFAULT NULL,
  `media_extensions` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `video_water` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `attach_size` int(11) NULL DEFAULT NULL,
  `attach_extensions` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `open_register` smallint(6) NULL DEFAULT NULL,
  `open_comment` smallint(6) NULL DEFAULT NULL,
  `comment_captcha` smallint(6) NULL DEFAULT NULL,
  `user_comment` smallint(6) NULL DEFAULT NULL,
  `guest_comment` smallint(6) NULL DEFAULT NULL,
  `comment_audit` smallint(6) NULL DEFAULT NULL,
  `comment_time_interval` int(11) NULL DEFAULT NULL,
  `open_cache` int(11) NULL DEFAULT NULL,
  `cache_time` int(11) NULL DEFAULT NULL,
  `pagination_number` int(11) NULL DEFAULT NULL,
  `celery_broker_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `celery_result_backend` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `admin_prefix` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `document_water` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `site_name`(`site_name`) USING BTREE,
  INDEX `ix_systems_is_active`(`is_active`) USING BTREE,
  INDEX `ix_systems_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of systems
-- ----------------------------
INSERT INTO `systems` VALUES (1, 0, 1, NULL, '2018-08-31 16:27:40', '杭州网媒体管理系统', '杭州网媒体管理系统', '杭州网媒体管理系统', '杭州网媒体管理系统', '浙备2018', '<script></script>', '版权所有 @2018', 'uploads', 'txt', 'water/logo.png', '杭州网', '40', 'water/font/fzls.ttf', '#ffffff', 1024, 'jpg|gif|png', 800, 800, 102400, 'mp4|mov|avi', '/static/demo.png', 102400, 'pdf|doc|zip|rar', 1, 1, 1, 1, 1, 1, 10, 1, 10, 10, 'amqp://root:root@localhost:5672/myvhost', 'redis://localhost:6379', 'admin', 1);

-- ----------------------------
-- Table structure for tags
-- ----------------------------
DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ix_tags_is_active`(`is_active`) USING BTREE,
  INDEX `ix_tags_is_delete`(`is_delete`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tags
-- ----------------------------
INSERT INTO `tags` VALUES (1, 0, 1, NULL, NULL, '美女', 'document');
INSERT INTO `tags` VALUES (2, 0, 1, NULL, NULL, '视频', 'video');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` smallint(6) NOT NULL,
  `is_active` smallint(6) NOT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nick_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `chinese_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sex` smallint(6) NULL DEFAULT NULL,
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qq` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `remarks` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_ip` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_time` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_count` int(11) NULL DEFAULT NULL,
  `group_id` int(11) NULL DEFAULT NULL,
  `integral` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_users_email`(`email`) USING BTREE,
  UNIQUE INDEX `ix_users_name`(`name`) USING BTREE,
  UNIQUE INDEX `ix_users_phone`(`phone`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE,
  INDEX `ix_users_is_active`(`is_active`) USING BTREE,
  INDEX `ix_users_is_delete`(`is_delete`) USING BTREE,
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (2, 0, 0, NULL, NULL, 'test001', 'test001@admin.com', 'pbkdf2:sha256:50000$CgAbhOWA$c2cc8c35c5851aaeb702d1039bae087d9d43d8e2be79ecc7e6d1de6201bb12fc', '', '', '', 0, '', '', '', '', '', 0, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
