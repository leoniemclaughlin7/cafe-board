
/** @jest-environment jsdom */


//https://stackoverflow.com/questions/72013449/upgrading-jest-to-v29-error-test-environment-jest-environment-jsdom-cannot-be
describe("Menu collapsible when title clicked", () => {

    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/menu.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });

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


});

//https://jestjs.io/docs/timer-mocks

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