import React from "react";
import { Route } from "react-router-dom";
import { Layout } from "antd";
import Splash from "./components/splash/splash";
import MainNavBar from "./components/main-nav-bar/main-nav-bar";
import "./App.css";

function App() {
  const Body = Layout;
  return (
    <Layout>
      <MainNavBar />
      <Body>
        <Route exact path="/" component={Splash} />
      </Body>
    </Layout>
  );
}

export default App;
