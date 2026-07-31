from flask import Blueprint, request, jsonify
from expense_service import (
    get_all_expenses,
    add_expense,
    delete_expense,
    filter_by_category,
    calculate_total,
)

expense_bp = Blueprint("expenses", __name__)


# Add Expense
@expense_bp.route("/expenses", methods=["POST"])
def create_expense():
    data = request.get_json()

    # Validation
    required_fields = ["title", "amount", "category", "date"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if data["amount"] <= 0:
        return jsonify({"error": "Amount must be greater than zero"}), 400

    expense = add_expense(data)

    return jsonify(expense), 201


# View All Expenses
@expense_bp.route("/expenses", methods=["GET"])
def view_expenses():

    category = request.args.get("category")

    if category:
        return jsonify(filter_by_category(category))

    return jsonify(get_all_expenses())


# Calculate Total
@expense_bp.route("/expenses/total", methods=["GET"])
def total_expenses():

    category = request.args.get("category")

    total = calculate_total(category)

    if category:
        return jsonify({
            "category": category,
            "total": total
        })

    return jsonify({
        "total": total
    })


# Delete Expense
@expense_bp.route("/expenses/<int:expense_id>", methods=["DELETE"])
def remove_expense(expense_id):

    deleted = delete_expense(expense_id)

    if deleted:
        return jsonify({
            "message": "Expense deleted successfully"
        })

    return jsonify({
        "error": "Expense not found"
    }), 404