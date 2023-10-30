start: logicalexpression;

logicalexpression:
     '\(' logicalexpression '\)'
    | '!' logicalexpression 
    |logicalexpression and logicalexpression
    |logicalexpression or logicalexpression
    |logicalexpression imp logicalexpression
    |true
    |false
    ;

and:    'and'
        |'\*'
        ;

or:     'or'
        |'\+'
        ;

imp:    '<=>'
        |'=>'
        ;

true :  'true'
        |'1'
        ;

false : 'false'
        |'0'
        ;

//Python comments
COMMENT: '\#''.*?''\n' (%ignore);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		