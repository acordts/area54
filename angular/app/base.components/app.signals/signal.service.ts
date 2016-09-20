/*
service returning promise
*/

import { Injectable } from '@angular/core';
import { Signal } from './signal';
import { SIGNALS } from './mock-signals';
@Injectable()
export class SignalService {
  getSignals(): Promise<Signal[]> {
    return Promise.resolve(SIGNALS);
  }
}