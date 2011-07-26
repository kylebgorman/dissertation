#!/usr/bin/env python
""" Copyright (c) 2011 Kyle Gorman

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

 Zipfian distribution sampling simulations 
 Kyle Gorman <kgorman@ling.upenn.edu>  
 Usage is described below. """

from sys import argv
from bisect import bisect
from random import random
from math import log, fsum
from collections import defaultdict


def sparse_dist(N, alpha=1, beta=0):
    return [(i + beta) ** -alpha for i in xrange(N, 0, -1)]


def mean(x):
    """ 
    Return arithmetic mean of a list of continuous values 
    """
    return fsum(x) / len(x)


def median(x, sorted=False):
    """ 
    Return median of an iterable of continuous values
    """
    my_x = x[:] # deep copy
    if not sorted:
        my_x.sort()
    if len(x) % 2 == 0: # even 
        l = len(my_x) / 2
        return (my_x[l - 1] + my_x[l]) / 2.
    else: # odd
        return my_x[len(my_x) // 2]


class ProbDist(object):

    def __init__(self, item2prob=None):
        """ 
        If item2prob is a list of positive reals, it will be normalized and 
        turned directly into a probability distribution. Otherwise we'll wait
        for increment and freq2prob to be called. 
        """
        self.prob = False
        if item2prob:
            self.item2freq = item2prob
            self.freq2prob()
        else:
            self.item2freq = defaultdict(int)

    def __str__(self):
        return '<ProbDist with %d types>' % len(self.item2freq)

    def __iter__(self):
        return iter(self.item2freq)

    def __getitem__(self, item):
        """ 
        Returns freq or prob of item 
        """
        return self.item2freq[item]

    def update(self, item_list):
        """ 
        Calls increment on each item in a list
        """
        if self.prob: 
            raise(ValueError, 'already probabilitized...sorry')
        for item in item_list:
            self.item2freq[item] += count

    def increment(self, item, count=1):
        if self.prob: 
            raise(ValueError, 'already probabilitized...sorry')
        self.item2freq[item] += count

    def freq2prob(self):
        """ 
        Convert from a frequency distribution to a probability distribution
        """
        if self.prob: 
            raise(ValueError, 'already probabilitized...sorry')
        # normalize, and build up backwards dist for sampling
        norm = float(sum(self.item2freq.values()))
        prob2items = defaultdict(list)
        for item in self.item2freq:
            p = self.item2freq[item] / norm # compute normalized prob
            self.item2freq[item] = p # write it in
            prob2items[p].append(item)
        self.prob2item = {} # different than defaultdict above
        self.probs = []
        adjuster = 0.
        for p in prob2items:
            for item in prob2items[p]:
                pa = p + adjuster
                self.probs.append(pa)
                self.prob2item[pa] = item
                adjuster = pa
        self.prob = True

    def sample(self):
        """ 
        Generate 1 random draw from the distribution 
        """
        if not self.prob:
            raise(ValueError, 'not yet probabilitized...sorry')
        assert self.prob, 'not yet probabilized: run freq2prob()'
        return self.prob2item[self.probs[bisect(self.probs, random())]]


def run_sim(n_types, n_tokens, n_iters=1, alpha=1, beta=0):
    """ 
    Where the magic happens... 
    """
    results = []

    # for n_trials iterations, do
    for i in xrange(n_iters):
        # generate a Zipfian distribution
        dist = ProbDist(dict(enumerate(sparse_dist(n_types, alpha, beta))))

        # sample from it Ntoken types
        observed = defaultdict(int)
        for i in xrange(n_tokens):
            observed[dist.sample()] # uses a trick here of defaultdicts...

        # compute results
        results.append(len(observed.values()))

    # return stats
    return (mean(results), median(results), min(results))


if __name__ == '__main__':
    try: 
        n_types = int(argv[1])
        n_tokens = int(argv[2])
        n_iters = int(argv[3])
        print '%d types sampled %d times for %d iterations' % (n_types,
                                                               n_tokens,
                                                               n_iters)
        if len(argv) == 5:
            alpha = float(argv[4])
            print 'alpha = %2.4f' % (alpha)
            print 'seen types: mean %d, median %d, min %d' % run_sim(n_types,
                                                                     n_tokens,
                                                                     n_iters,
                                                                     alpha)
        elif len(argv) == 6:
            alpha = float(argv[4])
            beta = float(argv[5])
            print 'alpha = %2.4f, beta = %2.4f' % (alpha, beta) 
            print 'seen types: mean %d, median %d, min %d' % run_sim(n_types,
                                                                     n_tokens,
                                                                     n_iters,
                                                                     alpha,
                                                                     beta)
        else:
            print 'seen types: mean %d, median %d, min %d' % run_sim(n_types,
                                                                     n_tokens,
                                                                     n_iters)
    except IndexError:
        print 'USAGE: sim.py Ntypes Ntokens Niters [alpha=1] [beta=1]'
    except ValueError:
        print 'Parameter values incorrect...quitting'
