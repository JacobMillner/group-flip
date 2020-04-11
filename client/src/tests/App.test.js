import React from "react";
import { shallow } from "enzyme";
import App from "../App";
import MainNavBar from "../components/main-nav-bar/main-nav-bar";

// App component tests tests
describe("App component testing", () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<App />);
  });

  test("App loads navbar", () => {
    expect(wrapper.find(MainNavBar)).toHaveLength(1);
  });
});
