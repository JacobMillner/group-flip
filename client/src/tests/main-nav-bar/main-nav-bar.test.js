import React from "react";
import { shallow } from "enzyme";
import { Menu } from "antd";
import MainNavBar from "../../components/main-nav-bar/main-nav-bar";

// App component tests tests
describe("Main navbar testing.", () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<MainNavBar />);
  });

  test("Navbar has menu", () => {
    expect(wrapper.find(Menu)).toHaveLength(1);
  });
});
