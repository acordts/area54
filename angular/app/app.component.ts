import { Component, OnInit } from '@angular/core';

import { Hero } from './hero';
import { HeroService } from './hero.service';

import { Signal } from './base.components/app.signals/signal';
import { SignalService } from './base.components/app.signals/signal.service';

@Component({
  selector: 'my-app',
  templateUrl: 'app/app.component.html',
  styleUrls:  ['app/app.component.css']
  providers: [
	HeroService, 
	SignalService
  ]
})
export class AppComponent implements OnInit {
  title = 'Tour of Heroes';
  heroes: Hero[];
  signals: Signal[];
  selectedHero: Hero;
  selectedSignal: Signal;

  constructor(private heroService: HeroService, private signalService: SignalService) { }

  getHeroes(): void {
    this.heroService.getHeroes().then(heroes => this.heroes = heroes);
  }

  getSignals(): void {
    this.signalService.getSignals().then(signals => this.signals = signals);
  }
  
  ngOnInit(): void {
    this.getHeroes();
	this.getSignals();
  }

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
  }

  onSelectSignal(signal: Signal): void {
    this.selectedSignal = signal;
  }
}
