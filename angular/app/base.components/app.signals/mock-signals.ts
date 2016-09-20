/*
Dummy signals
*/

import { Signal } from './signal';

export const SIGNALS: Signal[] = [
	{id: 1, signal: 'chat_msg', target: 'host'},
	{id: 2, signal: 'slide_next', target: 'client'},
	{id: 3, signal: 'chat_msg', target: 'client'},
	{id: 4, signal: 'chat_msg', target: 'client'},
]