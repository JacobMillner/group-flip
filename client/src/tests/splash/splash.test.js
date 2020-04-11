import React from "react";
import { shallow } from "enzyme";
import Splash from "../../components/splash/splash";

// App component tests tests
describe("Splash page testing.", () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallow(<Splash />);
  });

  test("Splash says hello world.", () => {
    expect(wrapper.text()).toEqual("Hello World!");
  });
});
