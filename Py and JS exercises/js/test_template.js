var expect = require('chai').expect;

var funcsToTest = require("./template");

const FREEFALL_TESTS = [
    { input: [1, true],
      output: "0.45"},
    { input: [0.45, false],
    output: "0.99"}
]

describe("freefall()", () => {
    FREEFALL_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input[0]}, ${t.input[1]})`, () => {
            expect(funcsToTest.freefall(...t.input)).to.be.eql(t.output);
        });
    });
});

const RPS_TESTS = [
    {input: 'RPS',
    output: 'PSR'},
    {input: 'PRSPRR',
    output: 'SPRSPP'}
];

describe("RPS()", () => {
    RPS_TESTS.forEach(t => {
        return it(`should return "${t.output}" when given the input ("${t.input}")`, () => {
            expect(funcsToTest.RPS(t.input)).to.be.eql(t.output);
        });
    });
});

const LIST2STR_TESTS = [
    {input: ['a',['b','c']], output:'[a[bc]]'},
    {input: ['a',['b',['c']]], output:'[a[b[c]]]'},
];

describe("list2str()", () => {
    LIST2STR_TESTS.forEach(t => {
        it(`should return "${t.output}" given the input (${JSON.stringify(t.input)})`, () => {
            expect(funcsToTest.list2str(t.input)).to.be.eql(t.output);
        });
    })
});

const TEXTPREPROCESSING_TESTS = [
    {input: 'I think, therefore I am.', output: ['think', 'therefore']},
    {input: 'When life gives you lemons, make lemonade.', output: ['life', 'give', 'you', 'lemon', 'make', 'lemonade']}
];

describe("textPreprocessing()", () => {
    TEXTPREPROCESSING_TESTS.forEach(t => {
        it(`should return ${JSON.stringify(t.output)} when given the input "${t.input}"`, () => {
            expect(funcsToTest.textPreprocessing(t.input)).to.have.deep.members(t.output);
        });
    });
});

const ISGREATERTHAN_TESTS = [
    {input: [{'a':1,'b':1},{'a':1,'b':1}], output: false},
    {input: [{'a':1,'b':0},{'a':0,'b':1}], output: false}
];

describe("isGreaterThan()", () => {
    ISGREATERTHAN_TESTS.forEach(t => {
        it(`should return ${t.output} when given the input(${JSON.stringify(t.input[0])},${JSON.stringify(t.input[1])})`, () => {
            expect(funcsToTest.isGreaterThan(...t.input)).to.be.eql(t.output);
        });
    });
});

const CSVSUM_TESTS = [
    {input: 'js/test_data/table1.csv', output: [5.0, 8.0, 6.0]},
    {input: 'js/test_data/table2.csv', output: [57.0, 518.0]}
];

describe("CSVsum()", () => {
    CSVSUM_TESTS.forEach(t => {
        it(`should return ${JSON.stringify(t.output)} when given the input ${t.input}`, () => {
            expect(funcsToTest.CSVsum(t.input)).to.have.deep.members(t.output);
        });
    });
});


const STR2LIST_TESTS = [
    {input: '[a[bc]]', output: ['a',['b','c']]},
    {input: '[a[b[c]]]', output: ['a',['b',['c']]]}
];

describe("str2list()", () => {
    STR2LIST_TESTS.forEach(t => {
        it(`should return ${JSON.stringify(t.output)} when given the input "${t.input}"`, () => {
            expect(funcsToTest.str2list(t.input)).to.have.deep.members(t.output);
        })
    });
});

const SPACEMON_TESTS = [
    {input: [[['Earth',100,10], ['Earth',100,10]], [['Mercury',80,10], ['Venus',80,10]]], output: false},
    {input: [[['Earth',100,10]], [['Mercury',80,10], ['Mars',80,10]]], output: true}
];

describe("spacemonSim()", () => {
    SPACEMON_TESTS.forEach(t => {
        it(`should return ${t.output} when given the input (${JSON.stringify(t.input[0])},${JSON.stringify(t.input[1])})`, () => {
            expect(funcsToTest.spacemonSim(...t.input)).to.be.equal(t.output);
        });
    });
});

const REWARDSHORTPATH_TESTS = [
    {input: [['A','X','R','R','R'],['O','O','O','X','B'],['O','O','O','O','R']], output: [7,3]},
    {input: [['A','X','R','R','R'],['O','O','O','X','R'],['O','O','O','B','R']], output: [5,0]}
];

describe("rewardShortPath()", () => {
    REWARDSHORTPATH_TESTS.forEach(t => {
        it(`should return ${JSON.stringify(t.output)} when given the input (${JSON.stringify(t.input)})`, () => {
            expect(funcsToTest.rewardShortPath(t.input)).to.have.deep.members(t.output);
        });
    })
});

const network1 = [[0,1,1,0,0,0,0],
[1,0,1,1,0,0,0],
[1,1,0,0,0,0,0],
[0,1,0,0,1,1,1],
[0,0,0,1,0,1,0],
[0,0,0,1,1,0,1],
[0,0,0,1,0,1,0]]

const network2 = [[0,1,0,0,0,0,1],
[1,0,0,0,0,0,1],
[0,0,0,1,0,0,1],
[0,0,1,0,0,0,1],
[0,0,0,0,0,1,1],
[0,0,0,0,1,0,1],
[1,1,1,1,1,1,0]]


const CLIQUECOUNTER_TESTS = [
    {input: network1, output: [1, 2, 1, 3, 1, 2, 1]},
    {input: network2, output: [1, 1, 1, 1, 1, 1, 3]}
];

describe("cliqueCounter()", () => {
    CLIQUECOUNTER_TESTS.forEach(t => {
        it(`should return ${JSON.stringify(t.output)} when given the input ${JSON.stringify(t.input)}`, () => {
            expect(funcsToTest.cliqueCounter(t.input)).to.have.deep.members(t.output);
        });
    });
});