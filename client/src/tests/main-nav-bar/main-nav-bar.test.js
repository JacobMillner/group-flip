import React from "react";
import Enzyme, { shallow, mount } from "enzyme";
import { Menu } from "antd";
import MainNavBar from "../../components/main-nav-bar/main-nav-bar";
import { BrowserRouter as Router } from "react-router-dom";

// App component tests tests
describe("Main navbar testing.", () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(
      <Router>
        <MainNavBar />
      </Router>
    );
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test("Has 'Home' menu option", () => {
    expect(wrapper.text()).toMatch(/Home/);
  });

  test("Has 'Select Book' menu option", () => {
    expect(wrapper.text()).toMatch(/Select Book/);
  });

  test("Menu Item becomes active when Select Book clicked", () => {
    expect(wrapper.find("#select-book").at(2).prop("isSelected")).toEqual(
      false
    );
    wrapper.find("#select-book").first().simulate("click");
    expect(wrapper.find("#select-book").at(2).prop("isSelected")).toEqual(
      true
    );
  });
});
