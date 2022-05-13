import random
import argparse
from matplotlib import pyplot as plt
from matplotlib import animation
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.shell_sort import shell_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.heap_sort import heap_sort
from algorithms.count_sort import count_sort
from algorithms.cocktail_sort import cocktail_sort
from algorithms.gnome_sort import gnome_sort
from algorithms.odd_even_sort import odd_even_sort
from algorithms.comb_sort import comb_sort


def update_fig(a, rects, iteration):
    """
     Function to update the plot
     :param a: the array with numbers
     :param rects: barrect for each number in the array
     :param iteration: the current iteration
     :return: None
     """
    for rect, val in zip(rects, a):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f'# of operations {iteration}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualizing sorting algorithms')
    parser.add_argument("-l", "--length", default=50, help="Count of numbers in the array", type=int)
    parser.add_argument("-s", "--speed", default=10, help="Set speed for animation", type=int)
    parser.add_argument("-a", "--algorithm", help="Sorting algorithm to animate", required=True,
                        choices=['bubble', 'cocktail', 'comb', 'count', 'gnome', 'heap', 'insertion', 'merge',
                                 'odd_even',
                                 'quick', 'selection', 'shell'])

    args = parser.parse_args()
    a = list(range(0, args.length))
    random.shuffle(a)

    if args.algorithm == 'bubble':
        generator = bubble_sort(a)
        name = 'Bubble Sort'
    elif args.algorithm == 'cocktail':
        generator = cocktail_sort(a, 0, len(a) - 1)
        name = 'Cocktail Shaker Sort'
    elif args.algorithm == 'comb':
        generator = comb_sort(a)
        name = 'Comb Sort'
    elif args.algorithm == 'count':
        generator = count_sort(a)
        name = 'Count Sort'
    elif args.algorithm == 'gnome':
        generator = gnome_sort(a)
        name = 'Gnome Sort'
    elif args.algorithm == 'heap':
        generator = heap_sort(a)
        name = 'Heap Sort'
    elif args.algorithm == 'insertion':
        generator = insertion_sort(a)
        name = 'Insertion Sort'
    elif args.algorithm == 'merge':
        generator = merge_sort(a, 0, len(a) - 1)
        name = 'Merge Sort'
    elif args.algorithm == 'odd_even':
        generator = odd_even_sort(a)
        name = 'Odd Even Sort'
    elif args.algorithm == 'quick':
        generator = quick_sort(a, 0, len(a) - 1)
        name = 'Quick Sort'
    elif args.algorithm == 'selection':
        generator = selection_sort(a)
        name = 'Selection Sort'
    elif args.algorithm == 'shell':
        generator = shell_sort(a)
        name = 'Shell Sort'
    else:
        pass

    fig, ax = plt.subplots()
    ax.set_title(name)
    bar_rects = ax.bar(range(len(a)), a, align='edge')
    ax.set_xlim(0, args.length)
    ax.set_ylim(0, int(1.07 * args.length))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    animate = animation.FuncAnimation(fig,
                                      func=update_fig,
                                      fargs=(bar_rects, iteration),
                                      frames=generator,
                                      interval=args.speed,
                                      repeat=False,
                                      save_count=1500
                                      )
    plt.show()


animate.to_html5_video()