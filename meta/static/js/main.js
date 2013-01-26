// models
var User = Backbone.Model.extend({
    schema: {
        name: 'Text',
        paycheck: 'Text',
        date_joined: 'Date'
    },

    validate: function(attrs){
        if (!attrs.name || !attrs.paycheck){
            return 'NOOOO';
        }
    },

    urlRoot: '/api/v1/users/'
});
var Room = Backbone.Model.extend({
    schema: {
        department: 'Text',
        spots: 'Text',
    },
    validate: function(attrs){
        if (!attrs.department || !attrs.spots){
            return 'NOOOO';
        }
    },
    urlRoot: '/api/v1/rooms/'
});


var Users = Backbone.Collection.extend({
    model: User,
    url: '/api/v1/users'
});
var Rooms = Backbone.Collection.extend({
    model: Room,
    url: '/api/v1/rooms'
});


// views
var user_template = _.template(_.unescape($('.user_view').html()));
var room_template = _.template(_.unescape($('.room_view').html()));


var BaseItemView = Backbone.View.extend({

    tagName: 'li',

    initialize: function(){
        this.model.bind('change', this.render, this);
        this.model.bind('destroy', this.remove, this);
    },

    showInput: function(event){
        var target = $(event.currentTarget);

        target.html(
            new EditWidget({container: target,
                            value: target.html(),
                            model: this.model}).$el
        );
    },

    showDateInput: function(event){
        var target = $(event.currentTarget);

        target.html(
            new DateWidget({container: target,
                            value: target.html(),
                            model: this.model}).$el
        );
    },

    render: function(){
        this.$el.html(
            this.template(this.model.toJSON())
        );
        return this;
    },

    delete: function(){
        this.model.destroy();
    }
});


var UserView = BaseItemView.extend({

    template: user_template,

    events: {
        'click .edit': 'showInput',
        'click .date': 'showDateInput',
        'click #delete': 'delete'
    }
});


var RoomView = BaseItemView.extend({

    template: room_template,

    events: {
        'click .edit': 'showInput',
        'click #delete': 'delete'
    },
});


var BaseView = Backbone.View.extend({
    hide: function(){
        this.$el.removeClass('active')
    },
    show: function(){
        this.$el.addClass('active')
    },
});


// forms
var Form = Backbone.Form.extend({
    save: function(callback){
        this.commit();
        this.model.save(this.model.toJSON(),
                        {success: function(model, resp){
                            callback(model);
                        }});
    }
});

var UserForm = new Form({
    model: new User,
});

var RoomForm = new Form({
    model: new Room
});


// views
var UsersView = BaseView.extend({
    el: $('#content .users'),

    initialize: function(){
        App.users.each(this.addOne);

        var form = this.$el.find('.form');
        form.append(UserForm.render().el);
    },

    addOne: function(user){
        if(App.users.get(user.id) == undefined) {
            App.users.add(user);
        }
        var user = new UserView({model: user});
        $('#users').append(user.render().el);
    }
});


var RoomsView = BaseView.extend({
    el: $('#content .rooms'),

    initialize: function(){
        App.rooms.each(this.addOne);

        var form = this.$el.find('.form');
        form.append(RoomForm.render().el);
    },

    addOne: function(room){
        var room = new RoomView({model:room});
        $('#rooms').append(room.render().el)
    },
});


var validators = {
    'int': jQuery.isNumeric,
    'date':  function(value){ return /^\d{1,2}\/\d{1,2}\/\d{4}$/.test(value) }
};

var EditWidget = Backbone.View.extend({

    tagName: 'input',
    className: 'text',
    events: {
        'keydown': 'save'
    },

    initialize: function(){
        this.options.container.removeClass('edit');
        this.$el.context.value = this.options.value;
        this.validator = this.options.container.data('type');
    },

    save: function(event){
        var container = this.options.container;
        var value = this.$el.context.value;
        var field = container.data('name')

        if(event.keyCode == 13 && this.validate(value)){
            container.addClass('edit');
            container.html(value);

            var data = {};
            data[field] = value;
            this.options.model.save(data);
        }
    },

    validate: function(value){
        if(!this.validator){
            return true;
        } else {
            console.log(validators[this.validator](value))
            if(validators[this.validator](value)){
                this.$el.css({'background': ''});
                return true;
            } else {
                this.$el.css({'background': 'red'});
                return false;
            }
        }
    }
});


var DateWidget = EditWidget.extend({
    initialize: function(){
        this.options.container.removeClass('date');
        this.$el.context.value = this.options.value;
        this.$el.datepicker();
        this.validator = this.options.container.data('type');
    },
});



// app
var App = Backbone.Router.extend({
    routes: {
        "": "default",
        "tab/:current": "getTab",
    },

    initialize: function(){
        var uview = new UsersView;
        var rview = new RoomsView;
        this.views = {"users": uview,
                      "rooms": rview}

        uview.$el.find('.addbtn').click(function(){
            UserForm.save(uview.addOne);
        });

        rview.$el.find('.addbtn').click(function(){
            RoomForm.save(rview.addOne);
        });
    },
    getTab: function(current) {
        _.each(this.views, function(view, name){
            ((name == current) ? view.show() : view.hide());
        });
    },
    default: function(){
        this.views['users'].show();
    }
});


$(function(){
    var app = new App();
    Backbone.history.start();
});
