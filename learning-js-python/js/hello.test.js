const hello = require("./hello");

describe("hello world test", () => {
  test("Returns hello string", () => {
    expect(hello.hello()).toBe("Hello");
  });
})