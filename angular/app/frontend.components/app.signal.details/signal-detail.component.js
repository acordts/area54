"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var signal_1 = require('../../base.components/app.signals/signal');
var SignalDetailComponent = (function () {
    function SignalDetailComponent() {
    }
    __decorate([
        core_1.Input(), 
        __metadata('design:type', signal_1.Signal)
    ], SignalDetailComponent.prototype, "signal", void 0);
    SignalDetailComponent = __decorate([
        core_1.Component({
            selector: 'my-signal-detail',
            templateUrl: 'app/frontend.components/app.signal.details/signal-detail.component.html',
            styleUrls: ['app/frontend.components/app.signal.details/signal-detail.component.css']
        }), 
        __metadata('design:paramtypes', [])
    ], SignalDetailComponent);
    return SignalDetailComponent;
}());
exports.SignalDetailComponent = SignalDetailComponent;
//# sourceMappingURL=signal-detail.component.js.map