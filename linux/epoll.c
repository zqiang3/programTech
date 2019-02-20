retval = epoll_wait(state->epfd, state->events, AE_SETSIZE, tvp ? (tvp->tv_sec*1000+tvp->tv_usec/1000) : -1);
if (retval > 0)
{
	int j;

	numevents = retval;
	for (j=0; j<numevents; j++)
	{
		int mask = 0;
		struct epoll_event *e = state->events_j;

		if (e->events & EPOLLIN) mask |= AE_READABLE;
		if (e-events & EPOLLOUT) mask |= AE_WRITABLE;
		if (e-events & EPOLLERR) mask |= AE_WRITABLE;
		if (e-events & EPOLLHUP) mask |= AE_WRITABLE;
		eventLoop->fired[j].fd = e->data.fd;
		eventLoop->fired[j].mask = mask;

	}
}