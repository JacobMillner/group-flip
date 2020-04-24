import React, { useState } from "react";
import { Menu } from "antd";
import { Link } from "react-router-dom";
import { VideoCameraOutlined, HomeOutlined } from "@ant-design/icons";

function MainNavBar(props) {
  const [menuSelect, setMenuSelect] = useState("home");

  const handleClick = (e) => {
    setMenuSelect(e.key);
  };

  return (
    <Menu onClick={handleClick} selectedKeys={[menuSelect]} mode="horizontal">
      <Menu.Item key="home" id="home">
        <Link to="/">
          <HomeOutlined />
          Home
        </Link>
      </Menu.Item>
      <Menu.Item key="select-book" id="select-book">
        <Link to="/select-book">
          <VideoCameraOutlined />
          Select Book
        </Link>
      </Menu.Item>
    </Menu>
  );
}

export default MainNavBar;
