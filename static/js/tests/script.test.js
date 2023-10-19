
/** @jest-environment jsdom */
import $ from 'jquery';
import { shallow } from 'enzyme';
import React from 'react';

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("templates/menu.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

// Render your component that contains the button
const wrapper = shallow(<button />);

// Find the button element within your component
const button = wrapper.find('collapseOne');

// Simulate a click event on the button
button.simulate('click');

//https://stackoverflow.com/questions/72013449/upgrading-jest-to-v29-error-test-environment-jest-environment-jsdom-cannot-be
describe("Menu collapsible when title clicked", () => {

    test('use jsdom in this test file', () => {
        const element = document.createElement('div');
        expect(element).not.toBeNull();
    });

    test("expect element by id collapseOne to exist", () => {
        const element = document.getElementById("collapseOne");
        expect(element).not.toBeNull();

    });

    test("expect element by id collapseTwo to exist", () => {
        const element = document.getElementById("collapseTwo");
        expect(element).not.toBeNull();

    });

    test("expect element by id collapseThree to exist", () => {
        const element = document.getElementById("collapseThree");
        expect(element).not.toBeNull();

    });

    test("should collapse menu collapsible when title clicked ", () => {
        const collapseSpy = jest.spyOn($.fn, 'collaspe');
        const wrapper = shallow(<button />);

        // Find the button element within your component
        const button = wrapper.find('collapseOne');

        // Simulate a click event on the button
        button.simulate('click');
        expect(collapseSpy).toHaveBeenCalledWith('toggle');
        collapseSpy.mockRestore();

    });




