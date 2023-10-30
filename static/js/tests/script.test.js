
/** @jest-environment jsdom */

// Tests for menu collapsibles 
describe("Menu collapsible when title clicked", () => {

    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/menu.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });

    test("expect element by id collapseOne to exist and collapse once clicked",
        () => {
            const element = document.getElementById("CollapsibleOne");
            const button = document.getElementById("collapseOne");
            expect(element).not.toBeNull();

            const hasToggleUnclicked = element.classList.contains('toggle');
            expect(hasToggleUnclicked).toBe(false);
            button.click();

            const hasToggleClicked = element.classList.contains('toggle');
            expect(hasToggleClicked).toBe(true);
        });

    test("expect element by id collapseTwo to exist", () => {
        const element = document.getElementById("collapseTwo");
        expect(element).not.toBeNull();
    });

    test("expect element by id collapseThree to exist", () => {
        const element = document.getElementById("collapseThree");
        expect(element).not.toBeNull();
    });
});

// Test for timeout function for messages, help from the links below. 
//https://jestjs.io/docs/timer-mocks
//https://stackoverflow.com/questions/77348090/testing-settimout-with-jest/77348344#77348344
jest.useFakeTimers();
jest.spyOn(global, 'setTimeout');
describe("Timer alerts and then closes after 3000", () => {

    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/base.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });

    test('closes the alert after 3 second via advanceTimersByTime', () => {
        const element = document.getElementById("msg");
        expect(element).not.toBeNull();
        expect(document.querySelector('.alert')).toBeTruthy();
        require('../script');
        setTimeout(() => {
            jest.runAllTimers();
            jest.advanceTimersByTime(3000);
            expect(setTimeout).toHaveBeenCalledTimes(1);
            expect(setTimeout).toHaveBeenLastCalledWith(expect.any(Function), 3000);
            expect(document.querySelector('.alert')).toBeNull();
        }, 3000);
    });
});