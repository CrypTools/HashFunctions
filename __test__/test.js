// Test made using EyeJS - https://eye.js.org
const pLib = require('path')
const md5 = pLib.normalize(__testDir + "/../MD5/JS/")
const sha256 = pLib.normalize(__testDir + "/../SHA256/JS/")

const md5hash = require(md5 + "encrypt.js")
const sha256hash = require(sha256 + "encrypt.js")

eye.describe("MD5", () => {
	eye.test("Hash", "node",
		$ => $(md5hash("Hello World!")).Equal("ed076287532e86365e841e92bfc50d8c")
	)
})
eye.describe("SHA256", () => {
	eye.test("Hash", "node",
		$ => $(sha256hash("Hello World!")).Equal("7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069")
	)
})
