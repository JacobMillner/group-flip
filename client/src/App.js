import React from "react";
import { Route } from "react-router-dom";
import { Layout } from "antd";
import Splash from "./components/splash/splash";
import MainNavBar from "./components/main-nav-bar/main-nav-bar";
import SelectBook from "./components/select-book/select-book";

import "./App.css";
function App() {
  const Body = Layout;
  const Footer = Layout;
  const Header = Layout;

  // TODO: move styling to App.js
  // TODO: use package.json for footer version
  // TODO: add tests for footer version number
  return (
    <Layout>
      <Header style={{ background: "#fff", padding: 0 }} />
      <MainNavBar />
      <Body style={{ minHeight: "92vh" }}>
        <Route exact path="/" component={Splash} />
        <Route exact path="/select-book/" component={SelectBook} />
      </Body>
      <Footer style={{ textAlign: "center" }}>Group Flip v0.1.1</Footer>
    </Layout>
  );
}

export default App;
