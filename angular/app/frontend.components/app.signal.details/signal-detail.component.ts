import { Component, Input } from '@angular/core';
import { Signal } from '../../base.components/app.signals/signal';

@Component({
  selector: 'my-signal-detail',
  templateUrl: 'app/frontend.components/app.signal.details/signal-detail.component.html',
  styleUrls:  ['app/frontend.components/app.signal.details/signal-detail.component.css']
})
export class SignalDetailComponent {
  @Input() signal: Signal;
}
