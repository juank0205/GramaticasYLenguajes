start: logicalexpression;

//expression
logicalexpression:
     parexpr
    |neg
    |binexpr
    |dimpexpr
    |impexpr
    |variable
    |ifexpr
    |ifelseexpr
    ;

parexpr: OPAR logicalexpression CPAR;
neg: '!' logicalexpression;

//Variables   
variable: ID;

ID: '[a-z]+' (%unless
        AND1:   'and';
        AND2:   '\*';
        OR1:    'or';
        OR2:    '\+';
        IMP:    '=>';
        DIMP:   '<=>';
        OPAR:   '\(';
        CPAR:   '\)';
        IF:     'if';
        ELSE:   'else';
        THEN:   'then';
    );

// Binary basic expressions
binexpr:        
        logicalexpression andexpr logicalexpression
        |logicalexpression orexpr logicalexpression
        |logicalexpression impexpr logicalexpression
        ;

// Implication expression
impexpr: 
        logicalexpression IMP logicalexpression;

dimpexpr: 
        logicalexpression DIMP logicalexpression;

andexpr: AND1
        |AND2
        ;

orexpr: OR1
        |OR2
        ;


//Conditional expression
ifexpr: IF logicalexpression THEN logicalexpression; 
ifelseexpr: IF logicalexpression THEN logicalexpression ELSE logicalexpression; 

//Python comments
COMMENT: '\#''.*?''\n' (%ignore);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		