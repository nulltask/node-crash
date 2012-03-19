var crash = require('../');

describe("node-crash", function() {
  it('should expose .version', function() {
    crash.version.should.be.match(/[0-9]+\.[0-9]+\.[0-9]+/);
  });

  it('should to spoil anything', function() {
    crash.crash();
  });
});
