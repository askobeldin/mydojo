//create a new class
define(["dojo/_base/declare",
        "dojo/_base/window", 
        "dojo/dom-construct",
        "dojo/dom"
    ], function(declare, win, domConstruct, dom){
        return declare(null, {
            //constructor: function(/* Object */args){
            //  dojo.safeMixin(this, args);
            //  }
            //
            log : function(msg){
                if(!dom.byId('console')){
                    domConstruct.create('div', {id:'console'}, win.body());
                }
                dom.byId('console').innerHTML += "<div>" + "<span>log:</span> " + msg + "</div>";
            }
    });
});

